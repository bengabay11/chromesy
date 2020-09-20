from chromesy.dal.table_adapters.TopSitesTableAdapter import TopSitesTableAdapter
from chromesy.utils.singleton_meta import SingletonMeta


class TopSitesDBAdapter(metaclass=SingletonMeta):
    def __init__(self, db_connection):
        self._db_connection = db_connection
        self._top_sites_table_adapter = TopSitesTableAdapter(self._db_connection)

    @property
    def top_sites(self):
        return self._top_sites_table_adapter
