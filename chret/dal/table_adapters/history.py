from chret.dal.db_connection import DBConnection
from chret.dal.models.Download import Download
from chret.dal.models.History import History


class HistoryTableAdapter(DBConnection):
    def get_chrome_history(self):
        return self.select(History, serializable=True)

    def get_chrome_downloads(self):
        return self.select(Download, serializable=True)
