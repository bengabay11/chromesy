from operator import itemgetter

from .path import get_chrome_profile_picture_path


class ChromeDataAdapter(object):
    def __init__(self, file_adapter, logins_table_adapter, history_table_adapter, top_sites_table_adapter):
        self._file_adapter = file_adapter
        self._logins_table_adapter = logins_table_adapter
        self._history_table_adapter = history_table_adapter
        self._top_sites_table_adapter = top_sites_table_adapter

    def export_chrome_history(self, output_file_path):
        history = self._history_table_adapter.get_chrome_history(serializable=False)
        sorted_history = sorted(history, key=itemgetter('id'))
        self._file_adapter.write(sorted_history, output_file_path)

    def get_chrome_downloads(self):
        return self._history_table_adapter.get_chrome_downloads()

    def get_top_sites(self):
        return self._top_sites_table_adapter.get_top_sites()

    def get_google_profile_picture(self, user):
        return open(get_chrome_profile_picture_path(user), "rb")

    def export_chrome_credentials(self, output_file_path):
        credentials = self._logins_table_adapter.get_chrome_credentials()
        self._file_adapter.write(credentials, output_file_path)

    def import_chrome_credentials(self, credentials_file):
        credentials = self._file_adapter.read(credentials_file)
        self._logins_table_adapter.insert_chrome_credentials(credentials)
