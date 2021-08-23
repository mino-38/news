import argparse
import sys
import json
import os

class News:
    def __init__(self):
        from . import news_auth
        news_auth.init()
        self.api = news_auth.auth() #NewsApiClientのインスタンス
    
    def get_top_news(self, sources=None, language="en", country="us"):
        """
        トップニュースを取得
        """
        if sources:
            country = language = None
            sources = sources[0]
        return self.api.get_top_headlines(sources=sources, language=language, country=country)

    def get_news(self, sources=None, q=None, from_param=None, to=None, page=1):
        """
        記事を検索
        """
        if sources:
            sources = sources[0]
        return self.api.get_everything(sources=sources, q=q, from_param=from_param, to=to, page=page)

    def get_all_source(self):
        """
        sources引数に渡せるソースを全て取得
        """
        for s in self.api.get_sources().get("sources"):
            output(s, key=None)

class config:
    file = os.path.join(os.path.dirname(__file__), "setting.json")
    with open(file, "r") as f:
        data = json.load(f)

    def save(self):
        """
        変更を保存
        """
        with open(self.file, "w") as f:
            json.dump(self.data, f)

    def reconfig(self):
        """
        国と言語の再設定
        """
        from . import news_auth
        news_auth.reset_apikey()
        self.data["country"] = input("Please enter the country code of the country you want to set: ").lower() or self.data.get("country")
        self.data["language"] = input("Please enter up to the second character of the language you want to set: ").lower() or self.data.get("language")
        self.save()

def output(data, key="articles"):
    """
    出力
    """
    if key:
        iter_data = data.get(key)
    else:
        iter_data = data
    def turn(d):
        for key, value in d.items():
            if key == "source":
                print(f"id: {value.get('id')}\nsource: {value.get('name')}")
            else:
                print(f"{key}: {value}")
        print()

    if isinstance(iter_data, list):
        for i in iter_data:
            turn(i)
    else:
        turn(iter_data)

def argument():
    parser = argparse.ArgumentParser(argument_default=None, description="Get news.")
    subparsers = parser.add_subparsers()
    parser.add_argument("-c", "--reconfig", action="store_true", help="Reset the language and country.")
    parser_search = subparsers.add_parser("search", help="It search articles.")
    parser_search.add_argument("words", default=None)
    parser_search.add_argument("-t", "--time", nargs=2, metavar=("[from]", "[to]"), help="Specify the article to get by date.\nIf there is only one argument, the article will be acquired in the range from the specified date to the current date.")
    parser.add_argument("-s", "--source", nargs=1, help="Specify the site to get the article.")
    parser.add_argument("-a", "--all-source", action="store_true", help="Get all source data.")
    return parser.parse_args()

def main():
    args = argument()
    c = config()
    if args.reconfig:
        c.reconfig()
        sys.exit()
    news = News()
    if args.all_source:
        news.get_all_source()
        sys.exit()
    try:
        zfill = lambda string: string.zfill(2)
        from_ = "-".join(map(zfill, args.time[0].split("-")))
        to = "-".join(map(zfill, args.time[1].split("-")))
    except (TypeError, AttributeError):
        from_ = to = None
    try:
        words = args.words
    except AttributeError:
        words = None
    if words:
        data = news.get_news(args.source, words, from_, to)
    else:
        data = news.get_top_news(args.source, c.data.get("language"), c.data.get("country"))
    output(data)

if __name__ == "__main__":
    main()