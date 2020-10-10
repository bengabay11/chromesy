import pandas as pd

from chpass.services.interfaces.IFileAdapter import IFileAdapter


class JsonFileAdapter(IFileAdapter):
    def write(self, data_list: list, output_file_path: str) -> None:
        df = pd.DataFrame(data_list)
        df.to_json(output_file_path)

    def read(self, path: str, converters: dict) -> list:
        df = pd.read_json(path)
        data = [dict(row[1]) for row in df.iterrows()]
        for row in data:
            for column, convert_callback in converters.items():
                row[column] = convert_callback(row[column])
        return data
