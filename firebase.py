import glob
import json
import logging
import os
from os.path import join, dirname
import time

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

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

# logging settings
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(name)10s:%(lineno)4d:%(levelname)s:%(message)s'))
logger.addHandler(handler)

# .env file settings
from dotenv import load_dotenv
load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# config file settings
import configparser
config = configparser.ConfigParser()
config.read('./config.ini')
try:
    FIREBASE_URL = config["firebase"]["url"]
except KeyError:
    pass


class Firebase(object):
    def __init__(self):
        if FIREBASE_URL == "":
            logger.error("FirebaseのURLが指定されていません")
            return
        self.database_url = FIREBASE_URL
        self._get_credentials()
        self.ref = db.reference()

    @staticmethod
    def _make_auth_file_from_datas(data):
        """
        辞書型データから認証用jsonファイルを作成

        Parameters
        ----------
        data : dict
            認証用の辞書型データ
        """
        with open('./firebase_auth.json', 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def _make_auth_file_from_dotenv():
        """
        .envファイルもしくは環境変数から認証用jsonファイルを作成

        See Also
        --------
        .envファイルもしくは環境変数の与え方については.env.sampleを参照
        """
        d = {
            "type": os.environ.get("FIREBASE_TYPE"),
            "project_id": os.environ.get("FIREBASE_PROJECT_ID"),
            "private_key_id": os.environ.get("FIREBASE_PRIVATE_KEY_ID"),
            "private_key": os.environ.get("FIREBASE_PRIVATE_KEY"),
            "client_email": os.environ.get("FIREBASE_CLIENT_EMAIL"),
            "client_id": os.environ.get("FIREBASE_CLIENT_ID"),
            "auth_uri": os.environ.get("FIREBASE_AUTH_URI"),
            "token_uri": os.environ.get("FIREBASE_TOKEN_URI"),
            "auth_provider_x509_cert_url": os.environ.get("FIREBASE_AUTH_PROVIDER_X509_CERT_URL"),
            "client_x509_cert_url": os.environ.get("FIREBASE_CLIENT_X509_CERT_URL")
        }
        with open('./firebase_auth.json', 'w') as f:
            json.dump(d, f, indent=4)

    @staticmethod
    def _check_path(path) -> bool:
        """
        Firebaseのデータの階層の判定

        Parameters
        ----------
        path : str
            相対パスの文字列

        Returns
        -------
        bool
            パスがカレントかそうでないかの真偽値
        """
        if path == "":
            return False
        else:
            return True

    def _get_credentials(self):
        """
        Firebaseの接続の認証を取得
        Firebaseから発行されたjsonファイルが同じディレクトリにない場合は、
        .envファイル（環境変数）もしくはハードコーディングされたデータから
        認証ファイルを自動作成。
        """
        try:
            file_list = glob.glob('*.json')
            if file_list == []:
                if os.path.exists(dotenv_path):
                    self._make_auth_file_from_dotenv()
                    file_list = glob.glob('*.json')
                else:
                    self._make_auth_file_from_datas(FIREBASE_AUTH_DATA)
                    file_list = glob.glob('*.json')

            cred = credentials.Certificate("./" + file_list[0])

            if not firebase_admin._apps:
                firebase_admin.initialize_app(cred, {
                    'databaseURL': self.database_url,
                    'databaseAuthVariableOverride': {
                        'uid': 'my-service-worker'
                    }
                })
        except ValueError:
            logger.error(f"Firebaseの認証データを取得できませんでした")
        except Exception as e:
            logger.error(f"Firebaseへの接続を確立できませんでした\n{e}")

    def push(self, data, path=""):
        try:
            start = time.time()
            if self._check_path(path):
                self.ref.child(path).push(data)
            else:
                self.ref.push(data)
            end = time.time()
            logger.info("successfully data pushed. result - {:.2f}s".format(end - start))

        except Exception as e:
            logger.error(f'データのpushに失敗しました.\n{e}')

    def set(self, data, path=""):
        try:
            start = time.time()
            if self._check_path(path):
                self.ref.child(path).set(data)
            else:
                self.ref.set(data)
            end = time.time()
            logger.info("successfully set data. result - {:.2f}s".format(end - start))

        except Exception as e:
            logger.error(f'データのsetに失敗しました.\n{e}')

    def update(self, updates, path=""):
        try:
            start = time.time()
            if self._check_path(path):
                before = self.ref.child(path).get()
                self.ref.child(path).update(updates)
            else:
                before = self.ref.get()
                self.ref.update(updates)
            end = time.time()
            logger.info("successfully data updated. result - {:.2f}s".format(end - start))

        except ValueError:
            logger.error(f"updatesの値はkey, valueの辞書型で与える必要があります")
        except Exception as e:
            logger.error(f'データの更新に失敗しました.\n{e}')

    def get(self, path=""):
        try:
            data = None
            start = time.time()
            if self._check_path(path):
                data = self.ref.child(path).get()
            else:
                data = self.ref.get()
            end = time.time()
            logger.info("successfully got data. result - {:.2f}s".format(end - start))
            return data

        except Exception as e:
            logger.error(f'データの取得に失敗しました.\n{e}')

    def delete(self, key, path=""):
        updates = {key: {}}
        try:
            start = time.time()
            if self._check_path(path):
                self.ref.child(path).update(updates)
            else:
                self.ref.update(updates)
            end = time.time()
            logger.info("successfully data deleted. result - {:.2f}s".format(end - start))

        except Exception as e:
            logger.error(f'データの削除に失敗しました.\n{e}')