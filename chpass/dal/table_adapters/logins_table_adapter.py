from chpass.dal.db_connection import DBConnection
from chpass.dal.models.login import Login
from chpass.exceptions.login_not_found_exception import LoginNotFoundException


class LoginsTableAdapter(object):
    def __init__(self, db_connection: DBConnection) -> None:
        self._db_connection = db_connection

    def get_all_logins(self, serializable: bool = False) -> list:
        return self._db_connection.select(Login, serializable=serializable)

    def get_login(self, login_id: int, serializable: bool = False) -> Login:
        filters = (Login.id == login_id,)
        result = self._db_connection.select(Login, filters, serializable=serializable)
        if result:
            return result[0]
        else:
            raise LoginNotFoundException(login_id)

    def insert_login(self, credentials: dict) -> None:
        login = Login(**credentials)
        self._db_connection.insert(login)

    def delete_login(self, login_id: int) -> None:
        filters = (Login.id == login_id,)
        self._db_connection.delete(Login, filters)
