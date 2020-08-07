from chromesy.dal.db_connection import DBConnection
from chromesy.dal.models.Login import Login


class LoginsTableAdapter(DBConnection):
    def get_chrome_credentials(self, serializable=True):
        return self.select(Login, serializable=serializable)

    def insert_chrome_credentials(self, credentials: dict):
        for credential in credentials:
            x = Login(origin_url=123)
            self.insert(x)
