

class IFileAdapter(object):
    def write(self, data: list, output_file_path: str) -> None:
        raise NotImplementedError

    def read(self, path: str) -> dict:
        raise NotImplementedError
