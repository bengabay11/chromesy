from chret.dal.models.Login import Login


class LoginsTableAdapter(object):
    def __init__(self, db_connection):
        self._conn = db_connection

    def get_chrome_credentials(self):
        return self._conn.select(Login, serializable=True)

    def insert_chrome_credentials(self, credentials):
        pass
        # for credential in credentials:
        #     x = Login(**credential)
        #     self._conn.insert(Login(**credential))
