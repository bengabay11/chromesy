from typing import List


class IFileAdapter(object):
    def write(self, data: List[dict], output_file_path: str, byte_columns: list = None) -> None:
        raise NotImplementedError

    def read(self, path: str, byte_columns: list = None) -> list:
        raise NotImplementedError
