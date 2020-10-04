import os

from chpass.dal.ChromeDBAdapter import ChromeDBAdapter
from chpass.services.profile_picture import export_profile_picture
from chpass.services.file_adapters import csv
from chpass.config import (
    OUTPUT_CREDENTIALS_FILE,
    OUTPUT_HISTORY_FILE,
    OUTPUT_DOWNLOADS_FILE,
    OUTPUT_TOP_SITES_FILE,
    OUTPUT_PROFILE_PICTURE_FILE
)


def export_chrome_data(chrome_db_adapter: ChromeDBAdapter, user: str, destination_folder: str, all_data: bool) -> None:
    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)
    credentials = chrome_db_adapter.logins.logins.get_chrome_credentials()
    csv.write(credentials, f"{destination_folder}/{OUTPUT_CREDENTIALS_FILE}")
    if all_data:
        history = chrome_db_adapter.history.history.get_chrome_history()
        csv.write(history, f"{destination_folder}/{OUTPUT_HISTORY_FILE}")
        downloads = chrome_db_adapter.history.downloads.get_chrome_downloads()
        csv.write(downloads, f"{destination_folder}/{OUTPUT_DOWNLOADS_FILE}")
        top_sites = chrome_db_adapter.top_sites.top_sites.get_top_sites()
        csv.write(top_sites, f"{destination_folder}/{OUTPUT_TOP_SITES_FILE}")
        export_profile_picture(user, f"{destination_folder}/{OUTPUT_PROFILE_PICTURE_FILE}")


def import_chrome_data(chrome_db_adapter: ChromeDBAdapter, source_file_path: str) -> None:
    chrome_credentials = csv.read(source_file_path)
    for current_credentials in chrome_credentials:
        current_credentials["form_data"] = csv.read_str_bytes(current_credentials["form_data"])
        current_credentials["password_value"] = csv.read_str_bytes(current_credentials["password_value"])
        current_credentials["possible_username_pairs"] = csv.read_str_bytes(current_credentials["possible_username_pairs"])
        chrome_db_adapter.logins.logins.insert_chrome_credentials(current_credentials)
