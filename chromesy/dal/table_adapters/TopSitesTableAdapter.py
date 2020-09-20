from chromesy.dal.models.TopSite import TopSite


class TopSitesTableAdapter(object):
    def __init__(self, db_connection):
        self._db_connection = db_connection

    def get_top_sites(self, serializable=False):
        return self._db_connection.select(TopSite, serializable=serializable)
