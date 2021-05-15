from typing import List

import pandas as pd

from chpass.core.interfaces.file_adapter_interface import IFileAdapter
from chpass.services.bytes import convert_bytes_in_data


class JsonFileAdapter(IFileAdapter):
    def write(self, data: List[dict], output_file_path: str, byte_columns: list = None) -> None:
        convert_bytes_in_data(data, list, byte_columns)
        df = pd.DataFrame(data)
        df.to_json(output_file_path)

    def read(self, path: str, byte_columns: list = None) -> list:
        df = pd.read_json(path)
        data = [dict(row[1]) for row in df.iterrows()]
        convert_bytes_in_data(data, bytes, byte_columns)
        return data
