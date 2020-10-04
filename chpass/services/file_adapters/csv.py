import csv
from chpass.config import WRITE_FILE_MODE


def write(data: list, output_file_path: str) -> None:
    with open(output_file_path, WRITE_FILE_MODE) as csv_file:
        writer = csv.writer(csv_file)
        columns = data[0].keys()
        writer.writerow(columns)
        for i in data:
            for key, value in i.items():
                if isinstance(value, bytes):
                    i[key] = list(value)
                if isinstance(value, str):
                    i[key] = value.encode("utf-8")
            writer.writerow(i.values())


def read(path: str) -> list:
    with open(path) as csv_file:
        reader = csv.reader(csv_file)
        lines = list(reader)
        columns = lines[0]
        values_list = []
        for line in lines[1:]:
            if line:
                value = {}
                for i in range(len(columns)):
                    value[columns[i]] = line[i]
                values_list.append(value)
        return values_list


def read_str_bytes(str_bytes):
    list_str_bytes = str_bytes[1:-1].split(",")
    list_int_bytes = [int(str_byte) for str_byte in list_str_bytes]
    return bytes(list_int_bytes)
