from pattern_singleton import Singleton

from chpass.dal.db_connection import DBConnection
from chpass.dal.table_adapters.top_sites_table_adapter import TopSitesTableAdapter


class TopSitesDBAdapter(metaclass=Singleton):
    def __init__(self, db_connection: DBConnection) -> None:
        self._db_connection = db_connection
        self._top_sites_table_adapter = TopSitesTableAdapter(self._db_connection)

    @property
    def top_sites_table(self) -> TopSitesTableAdapter:
        return self._top_sites_table_adapter

    def close(self) -> None:
        self._db_connection.close()
