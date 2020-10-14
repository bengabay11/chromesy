from chpass.dal.DBConnection import DBConnection
from chpass.dal.table_adapters.DownloadsTableAdapter import DownloadsTableAdapter
from chpass.dal.table_adapters.HistoryTableAdapter import HistoryTableAdapter
from chpass.core.SingletonMeta import SingletonMeta


class HistoryDBAdapter(metaclass=SingletonMeta):
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
