import os

from chpass.dal.ChromeDBAdapter import ChromeDBAdapter
from chpass.dal.DBConnection import DBConnection
from chpass.dal.db_adapters.HistoryDBAdapter import HistoryDBAdapter
from chpass.dal.db_adapters.LoginsDBAdapter import LoginsDBAdapter
from chpass.dal.db_adapters.TopSitesTableAdapter import TopSitesDBAdapter
from chpass.services.encryption import ChromeEncryptionAdapter
from chpass.services.interfaces.IFileAdapter import IFileAdapter
from chpass.services.path import get_chrome_logins_path, get_chrome_history_path, get_chrome_top_sites_path
from chpass.services.profile_picture import export_profile_picture
from chpass.config import OUTPUT_PROFILE_PICTURE_FILE, PASSWORDS_FILE_BYTES_COLUMNS


def create_chrome_db_adapter(protocol, os_user: str) -> ChromeDBAdapter:
    logins_db_connection = DBConnection()
    history_db_connection = DBConnection()
    top_sites_db_connection = DBConnection()
    logins_db_connection.connect(protocol, get_chrome_logins_path(os_user))
    history_db_connection.connect(protocol, get_chrome_history_path(os_user))
    top_sites_db_connection.connect(protocol, get_chrome_top_sites_path(os_user))
    logins_db_adapter = LoginsDBAdapter(logins_db_connection)
    history_db_adapter = HistoryDBAdapter(history_db_connection)
    top_sites_db_adapter = TopSitesDBAdapter(top_sites_db_connection)
    return ChromeDBAdapter(logins_db_adapter, history_db_adapter, top_sites_db_adapter)


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
        output_file_paths: dict,
        chrome_encryption_adapter: ChromeEncryptionAdapter = None) -> None:
    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)
    credentials = chrome_db_adapter.logins_db.logins_table.get_chrome_credentials()
    for current_credentials in credentials:
        for bytes_column in PASSWORDS_FILE_BYTES_COLUMNS:
            current_credentials[bytes_column] = list(current_credentials[bytes_column])
        if chrome_encryption_adapter:
            encrypted_password = current_credentials["password_value"]
            current_credentials["password_value"] = chrome_encryption_adapter.decrypt_password(encrypted_password)
    file_adapter.write(credentials, f"{destination_folder}/{output_file_paths['passwords']}")
    if all_data:
        export_additional_chrome_data(chrome_db_adapter, user, destination_folder, file_adapter, output_file_paths)


def read_bytes_column_from_csv(bytes_column: str) -> bytes:
    list_str_bytes = bytes_column[1:-1].split(",")
    list_bytes = [int(str_bytes) for str_bytes in list_str_bytes]
    return bytes(list_bytes)


def import_chrome_data(
        chrome_db_adapter: ChromeDBAdapter,
        source_file_path: str,
        file_adapter: IFileAdapter,
        chrome_encryption_adapter: ChromeEncryptionAdapter = None) -> None:
    csv_converters = {}
    json_converters = {}
    for bytes_column in PASSWORDS_FILE_BYTES_COLUMNS:
        csv_converters[bytes_column] = read_bytes_column_from_csv
        json_converters[bytes_column] = lambda list_bytes: bytes(list_bytes)
    chrome_credentials = file_adapter.read(source_file_path, json_converters)
    for current_credentials in chrome_credentials:
        if chrome_encryption_adapter:
            plain_password = current_credentials["password_value"]
            current_credentials["password_value"] = chrome_encryption_adapter.encrypt_password(plain_password)
        chrome_db_adapter.logins_db.logins_table.insert_chrome_credentials(current_credentials)
