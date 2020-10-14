import os

import pytest

from chpass import CsvFileAdapter


DATA_LIST = [{
    "column1": "value1",
    "column2": "value2",
    "column3": "value3"
}]


def test_csv_write():
    output_file_path = "test.csv"
    csv_file_adapter = CsvFileAdapter()
    csv_file_adapter.write(DATA_LIST, output_file_path)
    assert os.path.exists(output_file_path)


def test_csv_read():
    output_file_path = "test.csv"
    csv_file_adapter = CsvFileAdapter()
    result_data_list = csv_file_adapter.read(output_file_path)
    assert result_data_list == DATA_LIST
    os.remove(output_file_path)


def test_csv_write_output_file_path_not_exist():
    with pytest.raises(FileNotFoundError):
        output_file_path = "not_exist/test.csv"
        csv_file_adapter = CsvFileAdapter()
        csv_file_adapter.write(DATA_LIST, output_file_path)
    assert not os.path.exists(output_file_path)


def test_csv_write_output_file_invalid_output_file_path():
    with pytest.raises(ValueError):
        output_file_path = -1
        csv_file_adapter = CsvFileAdapter()
        csv_file_adapter.write(DATA_LIST, output_file_path)
    assert not os.path.exists(output_file_path)


def test_csv_write_output_file_invalid_data_list():
    with pytest.raises(ValueError):
        data_list = "invalid data list"
        output_file_path = "test.csv"
        csv_file_adapter = CsvFileAdapter()
        csv_file_adapter.write(data_list, output_file_path)
    assert not os.path.exists(output_file_path)
