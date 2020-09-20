import csv
from chromesy import config


def write(data: list, output_file_path: str) -> None:
    with open(output_file_path, config.WRITE_FILE_MODE) as csv_file:
        writer = csv.writer(csv_file)
        columns = data[0].keys()
        writer.writerow(columns)
        for i in data:
            for key, value in i.items():
                if isinstance(value, str):
                    i[key] = value.encode("utf-8")
            writer.writerow(i.values())


def read(path: str) -> list:
    with open(path) as csv_file:
        reader = csv.reader(csv_file)
        return list(reader)
