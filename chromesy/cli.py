# -*- coding: utf-8 -*-
"""
    chromesy
    ~~~~~
    chromesy is a package for manipulate chrome browser data.
    :copyright: 2020 Ben Gabay
    :license: MIT, see LICENSE for more details.
"""
import argparse
import getpass
import sys

from . import config
from .chrome import export_chrome_data, import_chrome_data
from .chrome_data_adapter import ChromeDataAdapter
from .config import DEFAULT_EXPORT_DESTINATION_FOLDER
from .dal.table_adapters.history import HistoryTableAdapter
from .dal.table_adapters.logins import LoginsTableAdapter
from .dal.table_adapters.top_sites import TopSitesTableAdapter
from .file_adapters.csv_adapter import CsvFileAdapter
from .path import get_chrome_logins_path, get_chrome_history_path, get_chrome_top_sites_path


def create_import_parser(subparsers):
    parser_import = subparsers.add_parser(
        "import",
        description="imports a json file with the data to chrome",
    )
    parser_import.add_argument(
        "-f",
        "--from",
        dest="from_file",
        type=argparse.FileType("r", encoding="utf-8"),
        default=sys.stdin
    )


def create_export_parser(subparsers):
    parser_export = subparsers.add_parser(
        "export",
        description="outputs a json file with the data"
    )
    parser_export.add_argument(
        "-d",
        "--destination",
        dest="destination_folder",
        type=str,
        help="destination folder to export the files",
        default=DEFAULT_EXPORT_DESTINATION_FOLDER
    )


def create_arg_parser():
    parser = argparse.ArgumentParser(
        prog="chromesy",
        description="Import and Export chrome data",
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


def main():
    arg_parser = create_arg_parser()
    args = arg_parser.parse_args()

    csv_file_adapter = CsvFileAdapter()
    logins_table_adapter = LoginsTableAdapter()
    history_table_adapter = HistoryTableAdapter()
    top_sites_table_adapter = TopSitesTableAdapter()
    logins_table_adapter.connect(config.DB_PROTOCOL, get_chrome_logins_path(args.user))
    history_table_adapter.connect(config.DB_PROTOCOL, get_chrome_history_path(args.user))
    top_sites_table_adapter.connect(config.DB_PROTOCOL, get_chrome_top_sites_path(args.user))
    chrome_data_adapter = ChromeDataAdapter(
        csv_file_adapter,
        logins_table_adapter,
        history_table_adapter,
        top_sites_table_adapter
    )
    mode_actions = {
        "export": lambda: export_chrome_data(chrome_data_adapter, args.user, args.destination_folder),
        "import": lambda: import_chrome_data(chrome_data_adapter, args.user)
    }
    mode_actions[args.mode]()
