## pythonからFirebaseへの接続方法

---
### 📌｜ Step1.
共有のGoogleドライブよりFirebase認証(共通DB)用のjsonファイルをダウンロードする。

---
### 📌｜Step2.(このスクリプトを利用しない場合)
pipインストール等でfirebase-adminのライブラリをインストールする。
<br>DBのURLは`https://magiot.firebaseio.com/`
を利用してください。
<br>認証用のjsonファイルは、Step1のものを利用してください。
<br>このスクリプトを利用しない場合のステップはここで終了です。 ライブラリの使い方に関しては、下記の記事を参考にしてください。
<br>[参考記事(Qiita)](https://qiita.com/sai-san/items/24dbee74c5744033c330)

---
### 📌｜Step2.(このスクリプトを利用する場合)
このレポジトリの[firebase.py](https://github.com/broccolingual/firebase/blob/master/firebase.py)
をダウンロードし、ソースコード上部のデータ入力欄にStep1のjsonファイルの内容をコピーして貼り付ける。FIREBASE_URLには、`https://magiot.firebaseio.com/`
を貼り付ける。

<br>`firebase.py`
```python
# ~上部省略~
# ------データ入力欄------
# FIREBASE_URL (データベースのURLを記述)
FIREBASE_URL = ""

# FIREBASE認証データ (jsonファイルの内容をコピーして下に貼り付け)
FIREBASE_AUTH_DATA = {
  "type": "",
  "project_id": "",
  "private_key_id": "",
  "private_key": "",
  "client_email": "",
  "client_id": "",
  "auth_uri": "",
  "token_uri": "",
  "auth_provider_x509_cert_url": "",
  "client_x509_cert_url": ""
}
# ----------------------
# ~下部省略~
```

---
### 📌｜Step2.(このスクリプトを利用する場合(オプション))
#### `※環境変数を利用したい方向け`

セキュリティ的に環境変数を利用したい方は[.env.sample](https://github.com/broccolingual/firebase/blob/master/.env.sample)
を元に環境変数を設定して下さい。環境変数を設定するにはpipインストール等でpython-dotenvのライブラリをインストールする必要があります。
<br>`※.envファイルの利用も可能。`

---
### 📌｜Step3.(このスクリプトを利用する場合)
自分の作成したpythonプログラムからfirebase.pyをインポートし、Firebaseオブジェクトを作成する。Firebaseクラスで利用できるメソッドは以下の通りである。
<br>具体的な利用方法や各メソッドの引数の与え方の例については[sample.py](https://github.com/broccolingual/firebase/blob/master/sample.py)
をご覧ください。

---
## 利用可能なメソッド
```python
push(data, path) # データの格納(Keyは時系列データを含む任意のキーになる.)
update(updates, path) # データのアップデート(格納)
get(path) # データの取得
delete(key, path) # データの削除
```

`※各メソッドのpathは任意指定.無指定の場合は，ルートディレクトリ.`

---
## Firebaseのデータ構造
<br>`data/flag`: 各ギミックのフラグのデータが格納されています。
<br>`data/hint`: 送信するヒントのデータが格納されています。
<br>`data/log`: 各ギミックの通過時間などのログデータが格納されています。

`※細かい各データの入力形式については進行表を参照`

---
### 環境及び使用ライブラリ
<img src="https://img.shields.io/badge/Python-3.8.5-3776AB.svg?logo=python&style=for-the-badge&logoColor=white">
<img src="https://img.shields.io/badge/firebase--admin-4.4.0-FFCA28.svg?style=flat-square">
<img src="https://img.shields.io/badge/python--dotenv-4.4.0-430098.svg?style=flat-square">

---
### License
<img src="https://img.shields.io/badge/Lisence-MIT-ff7964.svg?style=for-the-badge">

---
### 製作者
<img src="https://img.shields.io/badge/Broccolingual-9acd32.svg?style=for-the-badge">
<img src="https://img.shields.io/badge/G--Mail-broccolingual@gmail.com-ffffff.svg?logo=gmail&style=flat-square">
