from typing import List

import pandas as pd

from chpass.config import CSV_ADAPTER_ENCODING
from chpass.services.interfaces.IFileAdapter import IFileAdapter


class CsvFileAdapter(IFileAdapter):
    def write(self, data_list: List[dict], output_file_path: str) -> None:
        df = pd.DataFrame(data_list)
        df.to_csv(output_file_path, index=False, encoding=CSV_ADAPTER_ENCODING)

    def read(self, path: str, converters: dict = None) -> list:
        df = pd.read_csv(path, encoding=CSV_ADAPTER_ENCODING, converters=converters)
        return [dict(row[1]) for row in df.iterrows()]
