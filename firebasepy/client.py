import glob
import re
import urllib.parse

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from .exceptions import *

class Firebase:
    def __init__(self, db_url, uid="my-service-worker"):
        self.db_url = db_url
        self.uid = uid

        self.cred_filepath = None
        self.cred = None
        self._get_credentials()

        self.root = db.reference()
        self.ref = None

    def _search_cred_filepath(self):
        file_list = [f for f in glob.glob("**/*.json", recursive=True)]
        for f in file_list:
            if re.search(r".*?firebase.*?.json", f):
                self.cred_filepath = f
                return
        return

    def _get_credentials(self):
        o = urllib.parse.urlparse(self.db_url)
        if o.scheme not in ["http", "https"]:
            raise ValueError(f"URL is wrong or missing. -> {self.db_url}")
            return

        self._search_cred_filepath()
        if self.cred_filepath is None:
            raise TokenFileNotFoundError("Firebase token file(json) is not found.")
            return
        
        self.cred = credentials.Certificate(self.cred_filepath)

        if not firebase_admin._apps:
            firebase_admin.initialize_app(self.cred, {
                'databaseURL': self.db_url,
                'databaseAuthVariableOverride': {
                    'uid': self.uid
                }
            })

    def get_ref(self, path):
        if self.cred is None:
            return
        
        self.ref = db.reference(path)
