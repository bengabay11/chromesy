from chret.dal.db_connection import DBConnection
from chret.dal.models.TopSite import TopSite


class TopSitesTableAdapter(DBConnection):
    def get_top_sites(self):
        return self.select(TopSite, serializable=True)
