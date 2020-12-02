import configparser
import glob
import logging

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)  # Loglevelの設定

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(name)s:%(lineno)d:%(levelname)s:%(message)s'))
logger.addHandler(handler)

config = configparser.ConfigParser()
config.read('./config.ini')


class Firebase(object):
    def __init__(self):
        self.database_url = config["firebase"]["url"]
        self._get_credentials()
        self.ref = db.reference()

    def _get_credentials(self):
        try:
            file_list = glob.glob('*.json')
            if file_list is None:
                logger.error('Firebaseの認証データが見つかりません.')
                return

            cred = credentials.Certificate("./" + file_list[0])

            if not firebase_admin._apps:
                firebase_admin.initialize_app(cred, {
                    'databaseURL': self.database_url,
                    'databaseAuthVariableOverride': {
                        'uid': 'my-service-worker'
                    }
                })

        except Exception as e:
            logger.error(f"Firebaseへの接続を確立できませんでした.\n{e}")

    @staticmethod
    def _check_path(path) -> bool:
        if path == "":
            return False

    def push(self, data, path=""):
        try:
            if self._check_path(path):
                self.ref.child(path).push(data)
            else:
                self.ref.push(data)

        except Exception as e:
            logger.error(f'データのpushに失敗しました.\n{e}')

    def set(self, data, path=""):
        try:
            if self._check_path(path):
                self.ref.child(path).set(data)
            else:
                self.ref.set(data)

        except Exception as e:
            logger.error(f'データのsetに失敗しました.\n{e}')

    def update(self, updates, path=""):
        try:
            if self._check_path(path):
                self.ref.child(path).update(updates)
            else:
                self.ref.update(updates)

        except Exception as e:
            logger.error(f'データの更新に失敗しました.\n{e}')

    def get(self, path=""):
        try:
            if self._check_path(path):
                return self.ref.child(path).get()
            else:
                return self.ref.get()

        except Exception as e:
            logger.error(f'データの取得に失敗しました.\n{e}')

    def delete(self, path=""):
        try:
            if self._check_path(path):
                self.ref.child(path).update({})
            else:
                self.ref.update({})
                
        except Exception as e:
            logger.error(f'データの削除に失敗しました.\n{e}')