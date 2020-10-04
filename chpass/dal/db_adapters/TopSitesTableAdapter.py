from chpass.dal.DBConnection import DBConnection
from chpass.dal.table_adapters.TopSitesTableAdapter import TopSitesTableAdapter
from chpass.utils.SingletonMeta import SingletonMeta


class TopSitesDBAdapter(metaclass=SingletonMeta):
    def __init__(self, db_connection: DBConnection) -> None:
        self._db_connection = db_connection
        self._top_sites_table_adapter = TopSitesTableAdapter(self._db_connection)

    @property
    def top_sites(self) -> TopSitesTableAdapter:
        return self._top_sites_table_adapter

    def close(self) -> None:
        self._db_connection.close()
