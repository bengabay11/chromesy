from chpass.dal.DBConnection import DBConnection
from chpass.dal.models.History import History


class HistoryTableAdapter(object):
    def __init__(self, db_connection: DBConnection) -> None:
        self._db_connection = db_connection

    def get_chrome_history(self, serializable: bool = True) -> list:
        return self._db_connection.select(History, serializable=serializable)
