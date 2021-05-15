from chpass.dal.db_connection import DBConnection
from chpass.dal.models.topSite import TopSite


class TopSitesTableAdapter(object):
    def __init__(self, db_connection: DBConnection) -> None:
        self._db_connection = db_connection

    def get_top_sites(self, serializable: bool = False) -> list:
        return self._db_connection.select(TopSite, serializable=serializable)
