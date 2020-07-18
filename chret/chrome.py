from .dal.table_adapters.history import HistoryTableAdapter
from .dal.table_adapters.logins import LoginsTableAdapter
from .dal.table_adapters.top_sites import TopSitesTableAdapter
from .path import get_chrome_profile_picture_path, get_chrome_history_path, \
    get_chrome_top_sites_path, get_chrome_logins_path


class ChromeDataAdapter(object):
    def __init__(self, file_adapter):
        self._file_adapter = file_adapter
        self._logins_table_adapter = LoginsTableAdapter()
        self._history_table_adapter = HistoryTableAdapter()
        self._top_sites_table_adapter = TopSitesTableAdapter()

    def _connect_dbs(self, user, db_protocol):
        self._logins_table_adapter.connect(db_protocol, get_chrome_logins_path(user))
        self._history_table_adapter.connect(db_protocol, get_chrome_history_path(user))
        self._top_sites_table_adapter.connect(db_protocol, get_chrome_top_sites_path(user))

    def get_chrome_history(self):
        return self._history_table_adapter.get_chrome_history()

    def get_chrome_downloads(self):
        return self._history_table_adapter.get_chrome_downloads()

    def get_top_sites(self):
        return self._top_sites_table_adapter.get_top_sites()

    def get_google_profile_picture(self, user):
        return open(get_chrome_profile_picture_path(user), "rb")

    def export_chrome_credentials(self, output_file):
        credentials = self._logins_table_adapter.get_chrome_credentials()
        self._file_adapter.write(credentials, output_file)

    def import_chrome_credentials(self, credentials_file):
        credentials = self._file_adapter.read(credentials_file)
        self._logins_table_adapter.insert_chrome_credentials(credentials)
