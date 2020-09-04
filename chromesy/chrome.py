from operator import itemgetter
from shutil import copyfile

from .path import get_chrome_profile_picture_path


class ChromeDataAdapter(object):
    def __init__(self, file_adapter, logins_table_adapter, history_table_adapter, top_sites_table_adapter):
        self._file_adapter = file_adapter
        self._logins_table_adapter = logins_table_adapter
        self._history_table_adapter = history_table_adapter
        self._top_sites_table_adapter = top_sites_table_adapter

    def export_history(self, output_file_path):
        history = self._history_table_adapter.get_chrome_history(serializable=True)
        self._file_adapter.write(history, output_file_path)

    def export_downloads(self, output_file_path):
        downloads = self._history_table_adapter.get_chrome_downloads()
        self._file_adapter.write(downloads, output_file_path)

    def export_top_sites(self, output_file_path):
        top_sites = self._top_sites_table_adapter.get_top_sites(serializable=True)
        self._file_adapter.write(top_sites, output_file_path)

    def export_credentials(self, output_file_path):
        credentials = self._logins_table_adapter.get_chrome_credentials()
        self._file_adapter.write(credentials, output_file_path)

    def import_credentials(self, credentials_file):
        credentials = self._file_adapter.read(credentials_file)
        self._logins_table_adapter.insert_chrome_credentials(credentials)

    def export_profile_picture(self, user, destination_path):
        source_path = get_chrome_profile_picture_path(user)
        copyfile(source_path, destination_path)
