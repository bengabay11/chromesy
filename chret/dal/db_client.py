from chret.dal.db_connection import DBConnection
from chret.dal.models.Download import Download
from chret.dal.models.Login import Login


class DBClient(DBConnection):
    def get_chrome_credentials(self):
        return self.select(Login, serializable=True)

    def import_chrome_credentials(self, credentials):
        pass

    def get_chrome_history(self):
        pass

    def get_chrome_top_sites(self):
        pass

    def get_chrome_downloads(self):
        return self.select(Download, serializable=True)
