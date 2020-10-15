

class IFileAdapter(object):
    def write(self, data_list: list, output_file_path: str, byte_columns: list = None) -> None:
        raise NotImplementedError

    def read(self, path: str, byte_columns: list = None) -> list:
        raise NotImplementedError
