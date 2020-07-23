from chromesy.dal.db_connection import DBConnection
from chromesy.dal.models.Download import Download
from chromesy.dal.models.History import History


class HistoryTableAdapter(DBConnection):
    def get_chrome_history(self):
        return self.select(History, serializable=True)

    def get_chrome_downloads(self):
        return self.select(Download, serializable=True)
