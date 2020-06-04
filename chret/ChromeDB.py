import os
import win32crypt

from chret.BaseDB import BaseDB

CHROME_FOLDER = "AppData\\Local\Google\\Chrome\\User Data\\Default"
LOGIN_FILE = "Login Data"
HISTORY_FILE = "History"


class ChromeAdapter(object):
    def __init__(self):
        self._home_directory = os.path.expanduser('~')
        self._history_db = None
        self._login_db = None
        self._init_connections()

    @property
    def login_db(self):
        return self._login_db

    @login_db.setter
    def login_db(self, new_login_db):
        self._login_db = new_login_db

    @property
    def history_db(self):
        return self._history_db

    @history_db.setter
    def history_db(self, new_history_db):
        self._history_db = new_history_db

    def _init_connections(self):
        self._history_db = BaseDB()
        self._history_db.connect(os.path.join(self._home_directory, CHROME_FOLDER, HISTORY_FILE))
        self._login_db = BaseDB()
        self._login_db.connect(os.path.join(self._home_directory, CHROME_FOLDER, LOGIN_FILE))

    def get_credentials(self):
        statement = "SELECT origin_url, username_value, password_value FROM logins"
        cursor = self._login_db.execute(statement)
        raw_credentials = cursor.fetchall()
        return [{
            "url": url,
            "username": username,
            "password": self.decrypt_password(password)
        } for url, username, password in raw_credentials]

    def decrypt_password(self, password):
        return win32crypt.CryptUnprotectData(password, None, None, None, 0)