

class IFileAdapter(object):
    def write(self, data: dict, output_file_path: str) -> None:
        raise NotImplementedError

    def read(self, path: str) -> dict:
        raise NotImplementedError
