from typing import List

import pandas as pd

from chpass.config import CSV_ADAPTER_ENCODING
from chpass.core.interfaces.file_adapter_interface import IFileAdapter
from chpass.services.bytes import str_bytes_to_bytes, convert_bytes_in_data


class CsvFileAdapter(IFileAdapter):
    def write(self, data: List[dict], output_file_path: str, byte_columns: list = None) -> None:
        convert_bytes_in_data(data, list, byte_columns)
        df = pd.DataFrame(data)
        df.to_csv(output_file_path, index=False, encoding=CSV_ADAPTER_ENCODING)

    def read(self, path: str, byte_columns: list = None) -> list:
        df = pd.read_csv(path, encoding=CSV_ADAPTER_ENCODING)
        data = [dict(row[1]) for row in df.iterrows()]
        convert_bytes_in_data(data, str_bytes_to_bytes, byte_columns)
        return data
