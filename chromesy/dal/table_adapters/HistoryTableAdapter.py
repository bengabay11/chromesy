from chromesy.dal.models.History import History


class HistoryTableAdapter(object):
    def __init__(self, db_connection):
        self._db_connection = db_connection

    def get_chrome_history(self, serializable=True):
        return self._db_connection.select(History, serializable=serializable)
