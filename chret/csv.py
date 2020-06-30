import csv
from . import config


def write_csv_file(data, output_file_path):
    with open(output_file_path, config.WRITE_FILE_MODE) as csv_file:
        writer = csv.writer(csv_file)
        for key, value in data.items():
            writer.writerow([key, value])


def read_csv_file(path):
    with open(path) as csv_file:
        reader = csv.reader(csv_file)
        return list(reader)
