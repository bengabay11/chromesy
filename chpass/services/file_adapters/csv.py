import pandas as pd

from chpass.config import CSV_ADAPTER_ENCODING


def write(data_list: list, output_file_path: str) -> None:
    df = pd.DataFrame(data_list)
    df.to_csv(output_file_path, index=False, encoding=CSV_ADAPTER_ENCODING)


def read(path: str, converters: dict) -> list:
    df = pd.read_csv(path, encoding=CSV_ADAPTER_ENCODING, converters=converters)
    return [dict(row[1]) for row in df.iterrows()]
