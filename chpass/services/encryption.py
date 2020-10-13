import base64
import json

import win32crypt
from Crypto.Cipher import AES

from chpass.config import READ_FILE_MODE
from chpass.services.path import get_chrome_local_state_path


class ChromeEncryptionAdapter(object):
    def __init__(self, user):
        self._user = user
        self._key = self._get_encryption_key()

    def _get_encryption_key(self):
        chrome_local_state = get_chrome_local_state_path(self._user)
        with open(chrome_local_state, READ_FILE_MODE, encoding="utf-8") as local_state_file:
            local_state = local_state_file.read()
            local_state = json.loads(local_state)
        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        key = key[5:]
        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

    def decrypt_password(self, password: str) -> None:
        iv = password[3:15]
        password = password[15:]
        cipher = AES.new(self._key, AES.MODE_GCM, iv)
        return cipher.decrypt(password)[:-16].decode()


    def encrypt_password(self, password: str) -> None:
        pass
