from chromesy.dal.models.Login import Login


class LoginsTableAdapter(object):
    def __init__(self, db_connection):
        self._db_connection = db_connection

    def get_chrome_credentials(self, serializable=True):
        return self._db_connection.select(Login, serializable=serializable)

    def insert_chrome_credentials(self, credentials: dict):
        for credential in credentials:
            x = Login(origin_url=123)
            self._db_connection.insert(x)
