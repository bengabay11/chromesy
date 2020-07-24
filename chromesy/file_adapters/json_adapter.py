import json

from chromesy.config import WRITE_FILE_MODE
from chromesy.interfaces.IFileAdapter import IFileAdapter


class JsonFileAdapter(IFileAdapter):
    def write(self, data, output_file_path):
        with open(output_file_path, WRITE_FILE_MODE) as output_file:
            json.dump(data, output_file)

    def read(self, path):
        return json.load(path)
