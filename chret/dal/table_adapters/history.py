from chret.dal.models.Download import Download
from chret.dal.models.History import History


class HistoryTableAdapter(object):
    def __init__(self, db_connection):
        self._conn = db_connection

    def get_chrome_history(self):
        return self._conn.select(History, serializable=True)

    def get_chrome_downloads(self):
        return self._conn.select(Download, serializable=True)