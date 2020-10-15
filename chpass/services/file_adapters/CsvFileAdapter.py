import pandas as pd

from chpass.config import CSV_ADAPTER_ENCODING
from chpass.core.interfaces.IFileAdapter import IFileAdapter


def str_bytes_to_bytes(str_bytes: str) -> bytes:
    list_str_bytes = str_bytes[1:-1].split(",")
    list_bytes = [int(str_bytes) for str_bytes in list_str_bytes]
    return bytes(list_bytes)


class CsvFileAdapter(IFileAdapter):
    def write(self, data_list: list, output_file_path: str, byte_columns: list = None) -> None:
        for row in data_list:
            for byte_column in byte_columns:
                row[byte_column] = list(row[byte_column])
        df = pd.DataFrame(data_list)
        df.to_csv(output_file_path, index=False, encoding=CSV_ADAPTER_ENCODING)

    def read(self, path: str, byte_columns: list = None) -> list:
        df = pd.read_csv(path, encoding=CSV_ADAPTER_ENCODING)
        data = [dict(row[1]) for row in df.iterrows()]
        for row in data:
            for byte_column in byte_columns:
                row[byte_column] = str_bytes_to_bytes(row[byte_column])
        return data
