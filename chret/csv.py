import csv

WRITE_FILE_MODE = "w"


def write_csv_file(data, output_file_path):
    with open(output_file_path, WRITE_FILE_MODE) as output_file:
        writer = csv.DictWriter(output_file, fieldnames=data.keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def read_csv_file(path):
    pass
