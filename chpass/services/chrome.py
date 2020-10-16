import os
from typing import List

from chpass.dal.ChromeDBAdapter import ChromeDBAdapter
from chpass.core.interfaces import IFileAdapter
from chpass.services.profile_picture import export_profile_picture
from chpass.config import OUTPUT_PROFILE_PICTURE_FILE, PASSWORDS_FILE_BYTES_COLUMNS, CREDENTIALS_ALREADY_EXIST_MESSAGE


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
    passwords_destination_path = f"{destination_folder}/{output_file_paths['passwords']}"
    file_adapter.write(credentials, passwords_destination_path, byte_columns=PASSWORDS_FILE_BYTES_COLUMNS)
    if all_data:
        export_additional_chrome_data(chrome_db_adapter, user, destination_folder, file_adapter, output_file_paths)


def filter_duplicate_credentials(chrome_db_adapter: ChromeDBAdapter, credentials_to_import: List[dict]) -> list:
    db_credentials = chrome_db_adapter.logins_db.logins_table.get_chrome_credentials()
    db_credential_signon_realms = [current_db_credentials["signon_realm"] for current_db_credentials in db_credentials]
    unique_credentials = []
    for credentials in credentials_to_import:
        if credentials["signon_realm"] not in db_credential_signon_realms:
            unique_credentials.append(credentials)
        else:
            print(CREDENTIALS_ALREADY_EXIST_MESSAGE.format(credentials["signon_realm"]))
    return unique_credentials


def import_chrome_data(chrome_db_adapter: ChromeDBAdapter, source_file_path: str, file_adapter: IFileAdapter) -> None:
    if not os.path.exists(source_file_path):
        raise FileNotFoundError(source_file_path)
    credentials_to_import = file_adapter.read(source_file_path, byte_columns=PASSWORDS_FILE_BYTES_COLUMNS)
    credentials_to_import = filter_duplicate_credentials(chrome_db_adapter, credentials_to_import)
    for current_credentials in credentials_to_import:
        chrome_db_adapter.logins_db.logins_table.insert_chrome_credentials(current_credentials)
