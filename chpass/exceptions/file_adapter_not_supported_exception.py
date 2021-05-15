

class FileAdapterNotSupportedException(Exception):
    def __init__(self, file_adapter_format: str) -> None:
        self._file_adapter_format = file_adapter_format
        message = f"the following file adapter format is not supported - {file_adapter_format}"
        super().__init__(message)

    @property
    def file_adapter_format(self) -> str:
        return self._file_adapter_format

    @file_adapter_format.setter
    def file_adapter_format(self, new_file_adapter_format: str) -> None:
        self._file_adapter_format = new_file_adapter_format
