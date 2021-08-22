from newsapi import NewsApiClient
from dotenv import load_dotenv
import os
import sys

def init():
    if not os.path.isfile(env_file):
        #APIキーがまだ登録されてない場合の処理
        key = input("Pleas enter API key of the NewsAPI: ")
        with open(env_file, "a") as f:
            f.write(f"NEWS_API_KEY={key}")
    load_dotenv(env_file)

def auth():
    """
    NewsApiClientインスタンスを返す
    """
    return NewsApiClient(api_key=os.environ.get("NEWS_API_KEY"))

def reset_apikey():
    """
    APIキーの再設定
    """
    try:
        os.remove(env_file)
    except FileNotFoundError:
        print("Before using this program, you need to get the API key of NewsAPI(https://newsapi.org/)\nHave you got it yet?\n", file=sys.stderr)
    init()

env_file = os.path.join(os.path.dirname(__file__), ".env")