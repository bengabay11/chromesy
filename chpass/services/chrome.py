import os

from chpass.dal.ChromeDBAdapter import ChromeDBAdapter
from chpass.core.interfaces import IFileAdapter
from chpass.services.profile_picture import export_profile_picture
from chpass.config import OUTPUT_PROFILE_PICTURE_FILE, PASSWORDS_FILE_BYTES_COLUMNS


def export_additional_chrome_data(
        chrome_db_adapter: ChromeDBAdapter,
        user: str,
        destination_folder: str,
        file_adapter: IFileAdapter,
        output_file_paths: dict) -> None:
    history = chrome_db_adapter.history_db.history_table.get_chrome_history()
    file_adapter.write(history, f"{destination_folder}/{output_file_paths['history']}")
    downloads = chrome_db_adapter.history_db.downloads_table.get_chrome_downloads()
    file_adapter.write(downloads, f"{destination_folder}/{output_file_paths['downloads']}")
    top_sites = chrome_db_adapter.top_sites_db.top_sites_table.get_top_sites()
    file_adapter.write(top_sites, f"{destination_folder}/{output_file_paths['top_sites']}")
    export_profile_picture(user, f"{destination_folder}/{OUTPUT_PROFILE_PICTURE_FILE}")


def export_chrome_data(
        chrome_db_adapter: ChromeDBAdapter,
        user: str,
        destination_folder: str,
        all_data: bool,
        file_adapter: IFileAdapter,
        output_file_paths: dict) -> None:
    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)
    credentials = chrome_db_adapter.logins_db.logins_table.get_chrome_credentials()
    for current_credentials in credentials:
        for bytes_column in PASSWORDS_FILE_BYTES_COLUMNS:
            current_credentials[bytes_column] = list(current_credentials[bytes_column])
    file_adapter.write(credentials, f"{destination_folder}/{output_file_paths['passwords']}")
    if all_data:
        export_additional_chrome_data(chrome_db_adapter, user, destination_folder, file_adapter, output_file_paths)


def read_bytes_column_from_csv(bytes_column: str) -> bytes:
    list_str_bytes = bytes_column[1:-1].split(",")
    list_bytes = [int(str_bytes) for str_bytes in list_str_bytes]
    return bytes(list_bytes)


def import_chrome_data(chrome_db_adapter: ChromeDBAdapter, source_file_path: str, file_adapter: IFileAdapter) -> None:
    csv_converters = {}
    json_converters = {}
    for bytes_column in PASSWORDS_FILE_BYTES_COLUMNS:
        csv_converters[bytes_column] = read_bytes_column_from_csv
        json_converters[bytes_column] = lambda list_bytes: bytes(list_bytes)
    chrome_credentials = file_adapter.read(source_file_path, json_converters)
    for current_credentials in chrome_credentials:
        chrome_db_adapter.logins_db.logins_table.insert_chrome_credentials(current_credentials)
