# -*- coding: utf-8 -*-
"""
    chromesy
    ~~~~~
    chromesy is a package for manipulate chrome browser data.
    :copyright: 2020 Ben Gabay
    :license: MIT, see LICENSE for more details.
"""
import os

from sqlalchemy.exc import OperationalError

from . import config
from .arg_parser import create_arg_parser
from .chrome import ChromeDataAdapter
from .config import DESTINATION_FOLDER
from .dal.table_adapters.history import HistoryTableAdapter
from .dal.table_adapters.logins import LoginsTableAdapter
from .dal.table_adapters.top_sites import TopSitesTableAdapter
from .file_adapters.csv_adapter import CsvFileAdapter
from .file_adapters.json_adapter import JsonFileAdapter
from .path import get_chrome_logins_path, get_chrome_history_path, get_chrome_top_sites_path


def export_chrome_data(chrome_data_adapter, user):
    if not os.path.exists(DESTINATION_FOLDER):
        os.mkdir(DESTINATION_FOLDER)
    chrome_data_adapter.export_credentials(f"{DESTINATION_FOLDER}/credentials.csv")
    chrome_data_adapter.export_history(f"{DESTINATION_FOLDER}/history.csv")
    chrome_data_adapter.export_profile_picture(user, f"{DESTINATION_FOLDER}/profile.jpg")
    chrome_data_adapter.export_top_sites(f"{DESTINATION_FOLDER}/top_sites.csv")
    chrome_data_adapter.export_downloads(f"{DESTINATION_FOLDER}/downloads.csv")


def import_chrome_data(chrome_data_adapter):
    pass


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
    try:
        if args.mode == "export":
            export_chrome_data(chrome_data_adapter, args.user)
        elif args.mode == "import":
            import_chrome_data(chrome_data_adapter)
    except OperationalError as e:
        print("chrome database is locked. close chrome and try again")