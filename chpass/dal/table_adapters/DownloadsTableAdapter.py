from chpass.dal.DBConnection import DBConnection
from chpass.dal.models.Download import Download


class DownloadsTableAdapter(object):
    def __init__(self, db_connection: DBConnection) -> None:
        self._db_connection = db_connection

    def get_chrome_downloads(self, serializable: bool = False) -> list:
        return self._db_connection.select(Download, serializable=serializable)
