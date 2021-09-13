# 使用する前に
[NewsAPIのAPIキーを取得してください](https://newsapi.org/)

# インストール
```bash
$ pip install git+https://github.com/mino-38/news.git
```

# 使い方
まず最初に初期設定をして下さい
```bash
$ news -c
# Pleas enter API key of the NewsAPI: 取得したAPIキーを入力(セキュリティ対策のため出力はされません)  
# Please enter the country code of the country you want to set: 設定したい国の国コードを入力(jpは使用できなかったためusを推奨)  
# Please enter up to the second character of the language you want to set: 設定したい言語を英語で2文字目まで入力(jaは使用できなかったためenを推奨)
```
最初にNewsAPIのAPIキーを入力して下さい  
それ以降の国と言語の設定は取得する見出しに関係するのですが特に意味はないため、理由がない限りusとenを入力してください(何も入力しなかった場合は自動的にusとenが指定されたものとします)  
言語の設定ですが、enでも日本語がしっかり出力されます  
また、間違って入力しても再び実行すれば再設定することができます  

# オプション

## -s, --source  
取得するニュースサイトを指定します  
指定出来るサイトは-a, --all-sourceオプションで確認できます

例:
```bash
$ news -s bbc-news
# >>> BBC NEWSのトップニュースを取得
```

## -a, --all-source  
-s, --sourceオプションで指定できるソースを全て表示します
-s, --sourceオプションには"id"の値を渡してください

例:
```bash
id: hoge
name: fuga
etc...

となっていてこれを指定したい場合

$ news -s hoge
```

## -c, --reconfig  
APIキーと国、言語の再設定をします

# サブコマンド
search [検索ワード]  
ニュースを検索して表示します

# searchコマンドのオプション

## -t, --time from to  
期間を指定して記事を取得します

例:
```bash
$ news -t 2021-4-04 2021-8-15 search hoge
# >>> 2021-04-04 から 2021-08-15までの期間のhogeというワードを含む記事を取得
```

# アンインストールする場合
僕が作ったこのプログラムがゴミで使えないなと思った場合のみ実行してください  
この操作をするとせっかくインストールしたこのプログラムが飛びますよ(警告)

```bash
$ pip uninstall news-get
```
これを実行すると最後の警告が出るのでyを押してください

# 仕様変更について
予告なく使用を変更する場合があります  
予めご了承下さい
