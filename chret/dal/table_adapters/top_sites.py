from chret.dal.models.TopSite import TopSite


class TopSitesTableAdapter(object):
    def __init__(self, db_connection):
        self._conn = db_connection

    def get_top_sites(self):
        return self._conn.select(TopSite, serializable=True)
