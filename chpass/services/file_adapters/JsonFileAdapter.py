import pandas as pd

from chpass.core.interfaces.IFileAdapter import IFileAdapter


class JsonFileAdapter(IFileAdapter):
    def write(self, data_list: list, output_file_path: str, byte_columns: list = None) -> None:
        if byte_columns is None:
            byte_columns = []
        for row in data_list:
            for byte_column in byte_columns:
                row[byte_column] = list(row[byte_column])
        df = pd.DataFrame(data_list)
        df.to_json(output_file_path)

    def read(self, path: str, byte_columns: list = None) -> list:
        if byte_columns is None:
            byte_columns = []
        df = pd.read_json(path)
        data = [dict(row[1]) for row in df.iterrows()]
        for row in data:
            for byte_column in byte_columns:
                row[byte_column] = bytes(row[byte_column])
        return data
