from chromesy.dal.db_connection import DBConnection
from chromesy.dal.models.Download import Download
from chromesy.dal.models.History import History


class HistoryTableAdapter(DBConnection):
    def get_chrome_history(self, serializable=True):
        return self.select(History, serializable=serializable)

    def get_chrome_downloads(self, serializable=True):
        return self.select(Download, serializable=serializable)
