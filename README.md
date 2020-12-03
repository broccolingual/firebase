## 利用方法

### Firebaseの設定

このツールはFirebase Realtime Databaseをより簡単に利用するためのツールです。
Firebaseとpython上でやり取りするためには、Firebase側での設定が必要です。

---
##### 1. アクセス権限の設定

Firebaseでプロジェクトを作成した後にRealtime Databaseのルールのページより、下記の画像ような記述で読み込み及び書き込みの設定を行う必要があります。
<br>

![rule](https://gyazo.com/5a21f9e01de4edad69cdbb2671c5a138.png)

---
##### 2. 認証用jsonファイルの生成

プロジェクトの設定ページのサービスアカウントのページより、pythonのオプションを選択して、新しい秘密鍵の生成を行う必要があります。
これによりダウンロードされたファイルは厳重に管理したうえで、実行ファイルと同じ階層においておく必要があります。
<br>`※jsonファイルの名前は任意でも可。同じディレクトリに別のjsonファイルがある場合は認識しない可能性があります。`
<br>

![json](https://gyazo.com/16016c874eb7e2e5790612033aeccdc2.png)

---
### Python上での呼び出し方
<br>
本体は

[firebase.py](https://github.com/broccolingual/firebase/blob/master/firebase.py)

となっています。
Firebaseとのやり取りを行うためにはデータベースの認証用にFirebaseから発行できるjsonファイルを実行ファイルと同じ階層においておく必要があります。
<br>
<br>※オブジェクトの生成にはDatabaseのURLが必要です。URLのフォーマットは以下のような形式です。
<br>https://YOUR-DATABASE-NAME.firebaseio.com/
<br>データベースのURLは，
`config.ini`
にあらかじめ書いておく必要があります。

```python
Firebase()
```

[firebase.py](https://github.com/broccolingual/firebase/blob/master/firebase.py)
をimportしてFirebaseオブジェクトを作る必要があります。

---
### ディレクトリの配置方法
```python
├main.py #メインの実行ファイル(例でいうtest.py)
├firebase.py # このレポジトリのファイル(本体)
└hoge.json # Firebaseの認証用jsonファイル(発行方法は上記)
```

---
### 利用可能なメソッド
```python
push(data, path) # データの格納(Keyは時系列データを含む任意のキーになる.)
update(updates, path) # データのアップデート(格納)
get(path) # データの取得
delete(key_name, path) # データの削除
```

`※各メソッドのpathは任意指定.無指定の場合は，ルートディレクトリ.`

具体的な利用方法や各メソッドの引数の与え方の例については[sample.py](https://github.com/broccolingual/firebase/blob/master/sample.py)
をご覧ください。

## 環境及び使用ライブラリ
python 3.8.5
<br>firebase-admin 4.4.0

## License
<img src="https://img.shields.io/badge/Lisence-MIT-ff7964.svg?style=for-the-badge">

## 製作者
Broccolingual
<br>G-Mail: broccolingual@gmail.com