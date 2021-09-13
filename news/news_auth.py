from newsapi import NewsApiClient
from dotenv import load_dotenv
import os
import sys

def init(set_apikey=True):
    if set_apikey and not os.path.isfile(env_file):
        reset_apikey()
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
    import getpass
    if not os.path.isfile(env_file):
        print("Before using this program, you need to get the API key of NewsAPI(https://newsapi.org/)\nHave you got it yet?\n", file=sys.stderr)
    key = getpass.getpass(prompt="Please enter API key of the NewsAPI: ")
    if key:
        with open(env_file, "w") as f:
            f.write(f"NEWS_API_KEY={key}\n")

env_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")