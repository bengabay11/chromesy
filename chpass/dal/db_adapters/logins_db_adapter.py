from pattern_singleton import Singleton

from chpass.dal.db_connection import DBConnection
from chpass.dal.table_adapters.logins_table_adapter import LoginsTableAdapter


class LoginsDBAdapter(metaclass=Singleton):
    def __init__(self, db_connection: DBConnection) -> None:
        self._db_connection = db_connection
        self._logins_table_adapter = LoginsTableAdapter(self._db_connection)

    @property
    def logins_table(self) -> LoginsTableAdapter:
        return self._logins_table_adapter

    def close(self) -> None:
        self._db_connection.close()
