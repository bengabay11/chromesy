import os

from chpass.dal.ChromeDBAdapter import ChromeDBAdapter
from chpass.services.profile_picture import export_profile_picture
from chpass.services.file_adapters import csv
from chpass.config import (
    OUTPUT_CREDENTIALS_FILE,
    OUTPUT_HISTORY_FILE,
    OUTPUT_DOWNLOADS_FILE,
    OUTPUT_TOP_SITES_FILE,
    OUTPUT_PROFILE_PICTURE_FILE,
    PASSWORDS_FILE_BYTES_COLUMNS
)


def export_chrome_data(chrome_db_adapter: ChromeDBAdapter, user: str, destination_folder: str, all_data: bool) -> None:
    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)
    credentials = chrome_db_adapter.logins_db.logins_table.get_chrome_credentials()
    for current_credentials in credentials:
        for bytes_column in PASSWORDS_FILE_BYTES_COLUMNS:
            if current_credentials[bytes_column]:
                current_credentials[bytes_column] = list(current_credentials[bytes_column])
    csv.write(credentials, f"{destination_folder}/{OUTPUT_CREDENTIALS_FILE}")
    if all_data:
        history = chrome_db_adapter.history_db.history_table.get_chrome_history()
        csv.write(history, f"{destination_folder}/{OUTPUT_HISTORY_FILE}")
        downloads = chrome_db_adapter.history_db.downloads_table.get_chrome_downloads()
        csv.write(downloads, f"{destination_folder}/{OUTPUT_DOWNLOADS_FILE}")
        top_sites = chrome_db_adapter.top_sites_db.top_sites_table.get_top_sites()
        csv.write(top_sites, f"{destination_folder}/{OUTPUT_TOP_SITES_FILE}")
        export_profile_picture(user, f"{destination_folder}/{OUTPUT_PROFILE_PICTURE_FILE}")


def read_bytes_column_from_csv(bytes_column: str) -> bytes:
    list_str_bytes = bytes_column[1:-1].split(",")
    list_bytes = [int(str_bytes) for str_bytes in list_str_bytes]
    return bytes(list_bytes)


def import_chrome_data(chrome_db_adapter: ChromeDBAdapter, source_file_path: str) -> None:
    converters = {}
    for bytes_column in PASSWORDS_FILE_BYTES_COLUMNS:
        converters[bytes_column] = read_bytes_column_from_csv
    chrome_credentials = csv.read(source_file_path, converters)
    for current_credentials in chrome_credentials:
        chrome_db_adapter.logins_db.logins_table.insert_chrome_credentials(current_credentials)
