from setuptools import setup

setup(
    name="news-get",
    packages=["news", "news_auth"],
    author="minomushi",
    description="Get news from NewsAPI",
    version="1.0.0",
    install_requires=[
        "newsapi-python"
    ],
    entry_points={
        "console_scripts": [
            "news = news.news:main"
        ]
    },
    url="https://github.com/mino-38/news",
    license="MIT",
    keywords="NewsAPI news"
)