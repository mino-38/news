from setuptools import setup

setup(
    name="news",
    author="minomushi",
    version="1.0.0",
    install_requires=[
        "newsapi-python"
    ],
    entry_points={
        "console_scripts": [
            "news = news.news:main"
        ]
    },
    url="https://github.com/mino-38/news"
)