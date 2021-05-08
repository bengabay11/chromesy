import getpass
import os
from shutil import copyfile
from typing import List, Callable

from chpass.dal.ChromeDBAdapter import ChromeDBAdapter
from chpass.core.interfaces import IFileAdapter
from chpass.config import OUTPUT_PROFILE_PICTURE_FILE, PASSWORDS_FILE_BYTES_COLUMNS, CREDENTIALS_ALREADY_EXIST_MESSAGE
from chpass.services.path import get_chrome_profile_picture_path


def generic_export(
        get_data_func: Callable,
        file_adapter: IFileAdapter,
        destination_folder: str,
        output_path: str) -> None:
    data = get_data_func(serializable=True)
    file_adapter.write(data, f"{destination_folder}/{output_path}")


def export_profile_picture(destination_path: str, user: str = getpass.getuser()) -> None:
    source_path = get_chrome_profile_picture_path(user)
    copyfile(source_path, destination_path)


def export_history(
        chrome_db_adapter: ChromeDBAdapter,
        file_adapter: IFileAdapter,
        destination_folder: str,
        output_path: str) -> None:
    generic_export(chrome_db_adapter.history_db.history_table.get_chrome_history, file_adapter, destination_folder,
                   output_path)


def export_downloads(
        chrome_db_adapter: ChromeDBAdapter,
        file_adapter: IFileAdapter,
        destination_folder: str,
        output_path: str) -> None:
    generic_export(chrome_db_adapter.history_db.downloads_table.get_chrome_downloads, file_adapter, destination_folder,
                   output_path)


def export_top_sites(
        chrome_db_adapter: ChromeDBAdapter,
        file_adapter: IFileAdapter,
        destination_folder: str,
        output_path: str) -> None:
    generic_export(chrome_db_adapter.top_sites_db.top_sites_table.get_top_sites, file_adapter, destination_folder,
                   output_path)


def export_passwords(
        chrome_db_adapter: ChromeDBAdapter,
        file_adapter: IFileAdapter,
        destination_folder: str,
        output_path: str) -> None:
    logins = chrome_db_adapter.logins_db.logins_table.get_all_logins(serializable=True)
    file_adapter.write(logins, f"{destination_folder}/{output_path}", byte_columns=PASSWORDS_FILE_BYTES_COLUMNS)


def export_chrome_data(
        chrome_db_adapter: ChromeDBAdapter,
        destination_folder: str,
        file_adapter: IFileAdapter,
        output_file_paths: dict,
        user: str = getpass.getuser(),
        export_kind: str = None) -> None:
    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)
    export_functions = {
        "passwords": lambda: export_passwords(chrome_db_adapter, file_adapter, destination_folder,
                                              output_file_paths["passwords"]),
        "history": lambda: export_history(chrome_db_adapter, file_adapter, destination_folder,
                                          output_file_paths["history"]),
        "downloads": lambda: export_downloads(chrome_db_adapter, file_adapter, destination_folder,
                                              output_file_paths["downloads"]),
        "top_sites": lambda: export_top_sites(chrome_db_adapter, file_adapter, destination_folder,
                                              output_file_paths["top_sites"]),
        "profile_pic": lambda: export_profile_picture(f"{destination_folder}/{OUTPUT_PROFILE_PICTURE_FILE}",
                                                      user)
    }
    if export_kind:
        export_functions[export_kind]()
    else:
        for export_func in export_functions.values():
            export_func()


def filter_existed_logins(chrome_db_adapter: ChromeDBAdapter, logins_to_import: List[dict]) -> list:
    db_logins = chrome_db_adapter.logins_db.logins_table.get_all_logins(serializable=True)
    db_logins_signon_realms = [db_login["signon_realm"] for db_login in db_logins]
    unique_logins = []
    for login in logins_to_import:
        if login["signon_realm"] not in db_logins_signon_realms:
            unique_logins.append(login)
        else:
            print(CREDENTIALS_ALREADY_EXIST_MESSAGE.format(login["signon_realm"]))
    return unique_logins


def import_chrome_data(chrome_db_adapter: ChromeDBAdapter, source_file_path: str, file_adapter: IFileAdapter) -> None:
    if not os.path.exists(source_file_path):
        raise FileNotFoundError(source_file_path)
    logins_to_import = file_adapter.read(source_file_path, byte_columns=PASSWORDS_FILE_BYTES_COLUMNS)
    unique_logins_to_import = filter_existed_logins(chrome_db_adapter, logins_to_import)
    for login in unique_logins_to_import:
        chrome_db_adapter.logins_db.logins_table.insert_login(login)
