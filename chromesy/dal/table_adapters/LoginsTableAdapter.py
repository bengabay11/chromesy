from chromesy.dal.DBConnection import DBConnection
from chromesy.dal.models.Login import Login


class LoginsTableAdapter(object):
    def __init__(self, db_connection: DBConnection) -> None:
        self._db_connection = db_connection

    def get_chrome_credentials(self, serializable: bool = True) -> list:
        return self._db_connection.select(Login, serializable=serializable)

    def insert_chrome_credentials(self, credentials: dict) -> None:
        login = Login(**credentials)
        self._db_connection.insert(login)
