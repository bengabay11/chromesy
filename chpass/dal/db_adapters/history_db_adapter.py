from pattern_singleton import Singleton

from chpass.dal.db_connection import DBConnection
from chpass.dal.table_adapters.downloads_table_adapter import DownloadsTableAdapter
from chpass.dal.table_adapters.history_table_adapter import HistoryTableAdapter


class HistoryDBAdapter(metaclass=Singleton):
    def __init__(self, db_connection: DBConnection) -> None:
        self._db_connection = db_connection
        self._history_table_adapter = HistoryTableAdapter(self._db_connection)
        self._downloads_table_adapter = DownloadsTableAdapter(self._db_connection)

    @property
    def history_table(self) -> HistoryTableAdapter:
        return self._history_table_adapter

    @property
    def downloads_table(self) -> DownloadsTableAdapter:
        return self._downloads_table_adapter

    def close(self) -> None:
        self._db_connection.close()
