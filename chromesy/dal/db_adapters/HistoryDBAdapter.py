from chromesy.dal.table_adapters.DownloadsTableAdapter import DownloadsTableAdapter
from chromesy.dal.table_adapters.HistoryTableAdapter import HistoryTableAdapter
from chromesy.utils.singleton_meta import SingletonMeta


class HistoryDBAdapter(metaclass=SingletonMeta):
    def __init__(self, db_connection):
        self._db_connection = db_connection
        self._history_table_adapter = HistoryTableAdapter(self._db_connection)
        self._downloads_table_adapter = DownloadsTableAdapter(self._db_connection)

    @property
    def history(self):
        return self._history_table_adapter

    @property
    def downloads(self):
        return self._downloads_table_adapter
