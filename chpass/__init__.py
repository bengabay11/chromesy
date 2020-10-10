# -*- coding: utf-8 -*-
"""
    chpass
    ~~~~~
    chpass is a package for export and import chrome browser passwords.
    :copyright: 2020 Ben Gabay
    :license: MIT, see LICENSE for more details.
"""

__version__ = '1.0.0'

from chpass.cli import create_arg_parser
from chpass.config import OUTPUT_FILE_PATHS, DB_PROTOCOL
from chpass.exceptions.FileAdapterNotSupportedException import FileAdapterNotSupportedException
from chpass.services.chrome import create_chrome_db_adapter, export_chrome_data, import_chrome_data
from chpass.services.file_adapters.csv import CsvFileAdapter
from chpass.services.file_adapters.json import JsonFileAdapter


def main() -> None:
    arg_parser = create_arg_parser()
    args = arg_parser.parse_args()
    file_adapters = {
        "json": JsonFileAdapter(),
        "csv": CsvFileAdapter()
    }
    if args.file_adapter not in file_adapters.keys():
        raise FileAdapterNotSupportedException(args.file_adapter)
    file_adapter = file_adapters[args.file_adapter]
    output_file_paths = OUTPUT_FILE_PATHS[args.file_adapter]
    chrome_db_adapter = create_chrome_db_adapter(DB_PROTOCOL, args.user)
    mode_actions = {
        "export": lambda: export_chrome_data(
            chrome_db_adapter,
            args.user,
            args.destination_folder,
            args.all_data,
            file_adapter,
            output_file_paths
        ),
        "import": lambda: import_chrome_data(chrome_db_adapter, args.from_file, file_adapter)
    }
    mode_actions[args.mode]()
    chrome_db_adapter.close()
