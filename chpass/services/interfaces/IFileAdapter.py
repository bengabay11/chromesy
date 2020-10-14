

class IFileAdapter(object):
    def write(self, data_list: list, output_file_path: str) -> None:
        raise NotImplementedError

    def read(self, path: str, converters: dict = None) -> list:
        raise NotImplementedError
