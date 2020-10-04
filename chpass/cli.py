# -*- coding: utf-8 -*-
"""
    chpass
    ~~~~~
    chpass is a package for export and import chrome browser passwords.
    :copyright: 2020 Ben Gabay
    :license: MIT, see LICENSE for more details.
"""

import argparse
import getpass


from .chrome import export_chrome_data, import_chrome_data
from .config import DEFAULT_EXPORT_DESTINATION_FOLDER, DB_PROTOCOL, DEFAULT_EXPORT_ALL_DATA
from .dal.ChromeDBAdapter import ChromeDBAdapter
from .dal.db_adapters.HistoryDBAdapter import HistoryDBAdapter
from .dal.db_adapters.LoginsDBAdapter import LoginsDBAdapter
from .dal.db_adapters.TopSitesTableAdapter import TopSitesDBAdapter
from .dal.DBConnection import DBConnection
from chpass.services.path import get_chrome_logins_path, get_chrome_history_path, get_chrome_top_sites_path


def create_import_parser(subparsers: argparse._SubParsersAction) -> None:
    parser_import = subparsers.add_parser(
        "import",
        description="imports a json file with the data to chrome",
    )
    parser_import.add_argument(
        "-f",
        "--from",
        dest="from_file",
        help="credentials file to import from",
        type=str,
        required=True
    )


def create_export_parser(subparsers: argparse._SubParsersAction) -> None:
    parser_export = subparsers.add_parser(
        "export",
        description="outputs a csv file with the data"
    )
    parser_export.add_argument(
        "-d",
        "--destination",
        dest="destination_folder",
        type=str,
        help="destination folder to export the files",
        default=DEFAULT_EXPORT_DESTINATION_FOLDER
    )
    parser_export.add_argument(
        "-a",
        "--all",
        dest="all_data",
        help="export all the data",
        action='store_true',
        default=DEFAULT_EXPORT_ALL_DATA
    )


def create_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="chpass",
        description="Import and Export chrome passwords",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="mode")
    subparsers.required = True
    create_import_parser(subparsers)
    create_export_parser(subparsers)
    parser.add_argument(
        "-u",
        "--user",
        dest="user",
        type=str,
        default=getpass.getuser()
    )
    return parser


def create_chrome_db_adapter(user: str) -> ChromeDBAdapter:
    logins_db_connection = DBConnection()
    history_db_connection = DBConnection()
    top_sites_db_connection = DBConnection()
    logins_db_connection.connect(DB_PROTOCOL, get_chrome_logins_path(user))
    history_db_connection.connect(DB_PROTOCOL, get_chrome_history_path(user))
    top_sites_db_connection.connect(DB_PROTOCOL, get_chrome_top_sites_path(user))
    logins_db_adapter = LoginsDBAdapter(logins_db_connection)
    history_db_adapter = HistoryDBAdapter(history_db_connection)
    top_sites_db_adapter = TopSitesDBAdapter(top_sites_db_connection)
    return ChromeDBAdapter(
        logins_db_adapter,
        history_db_adapter,
        top_sites_db_adapter
    )


def main() -> None:
    arg_parser = create_arg_parser()
    args = arg_parser.parse_args()
    chrome_db_adapter = create_chrome_db_adapter(args.user)
    mode_actions = {
        "export": lambda: export_chrome_data(chrome_db_adapter, args.user, args.destination_folder, args.all_data),
        "import": lambda: import_chrome_data(chrome_db_adapter, args.from_file)
    }
    mode_actions[args.mode]()
    chrome_db_adapter.close()