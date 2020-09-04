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
from .dal.table_adapters.history import HistoryTableAdapter
from .dal.table_adapters.logins import LoginsTableAdapter
from .dal.table_adapters.top_sites import TopSitesTableAdapter
from .file_adapters.csv_adapter import CsvFileAdapter
from .file_adapters.json_adapter import JsonFileAdapter
from .path import get_chrome_logins_path, get_chrome_history_path, get_chrome_top_sites_path


def main():
    arg_parser = create_arg_parser()
    args = arg_parser.parse_args()
    user = "~"

    csv_file_adapter = CsvFileAdapter()
    logins_table_adapter = LoginsTableAdapter()
    history_table_adapter = HistoryTableAdapter()
    top_sites_table_adapter = TopSitesTableAdapter()

    logins_table_adapter.connect(config.DB_PROTOCOL, get_chrome_logins_path(user))
    history_table_adapter.connect(config.DB_PROTOCOL, get_chrome_history_path(user))
    top_sites_table_adapter.connect(config.DB_PROTOCOL, get_chrome_top_sites_path(user))

    chrome_data_adapter = ChromeDataAdapter(
        csv_file_adapter,
        logins_table_adapter,
        history_table_adapter,
        top_sites_table_adapter
    )

    if not os.path.exists("dist"):
        os.mkdir("dist")
    try:
        if args.mode == "export":
            chrome_data_adapter.export_credentials("dist/credentials.csv")
            chrome_data_adapter.export_history("dist/history.csv")
            chrome_data_adapter.export_profile_picture("~", "dist/profile.jpg")
            chrome_data_adapter.export_top_sites("dist/top_sites.csv")
            chrome_data_adapter.export_downloads("dist/downloads.csv")
    except OperationalError as e:
        print("chrome database is locked. close chrome and try again")
