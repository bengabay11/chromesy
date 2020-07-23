import csv
from chromesy import config
from chromesy.interfaces.IFileAdapter import IFileAdapter


class CsvFileAdapter(IFileAdapter):
    def write(self, data, output_file_path):
        with open(output_file_path, config.WRITE_FILE_MODE) as csv_file:
            writer = csv.writer(csv_file)
            for i in data:
                for key, value in i.items():
                    writer.writerow([key, value])

    def read(self, path):
        with open(path) as csv_file:
            reader = csv.reader(csv_file)
            return list(reader)
