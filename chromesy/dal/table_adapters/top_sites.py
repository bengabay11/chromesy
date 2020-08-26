from chromesy.dal.db_connection import DBConnection
from chromesy.dal.models.TopSite import TopSite


class TopSitesTableAdapter(DBConnection):
    def get_top_sites(self, serializable=False):
        return self.select(TopSite, serializable=serializable)
