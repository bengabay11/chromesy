from chret.dal.db_connection import DBConnection
from chret.dal.models.Login import Login


class DBClient(DBConnection):
    def get_chrome_credentials(self):
        return self.select(Login)

