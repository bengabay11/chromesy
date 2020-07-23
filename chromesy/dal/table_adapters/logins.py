from chromesy.dal.db_connection import DBConnection
from chromesy.dal.models.Login import Login


class LoginsTableAdapter(DBConnection):
    def get_chrome_credentials(self):
        return self.select(Login, serializable=True)

    def insert_chrome_credentials(self, credentials):
        pass
        # for credential in credentials:
        #     x = Login(**credential)
        #     self.insert(x)
