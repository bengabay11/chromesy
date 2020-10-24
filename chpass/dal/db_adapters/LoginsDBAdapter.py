from py_singleton import singleton

from chpass.dal.DBConnection import DBConnection
from chpass.dal.table_adapters.LoginsTableAdapter import LoginsTableAdapter


@singleton
class LoginsDBAdapter(object):
    def __init__(self, db_connection: DBConnection) -> None:
        self._db_connection = db_connection
        self._logins_table_adapter = LoginsTableAdapter(self._db_connection)

    @property
    def logins_table(self) -> LoginsTableAdapter:
        return self._logins_table_adapter

    def close(self) -> None:
        self._db_connection.close()
