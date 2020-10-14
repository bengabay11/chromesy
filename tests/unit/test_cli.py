import getpass

import pytest

from chpass import parse_args


@pytest.fixture(autouse=True)
def export_mode() -> str:
    return "export"


@pytest.fixture(autouse=True)
def import_mode() -> str:
    return "import"


@pytest.fixture(autouse=True)
def from_file() -> str:
    return "passwords.csv"


def test_default_export(export_mode):
    args = parse_args([export_mode])
    assert args.mode == export_mode
    assert not args.all_data
    assert args.user == getpass.getuser()
    assert args.destination_folder == "dist"
    assert args.file_adapter == "csv"
    assert not hasattr(args, "from_file")


def test_default_import(import_mode, from_file):
    args = parse_args([import_mode, "-f", from_file])
    assert args.mode == import_mode
    assert not hasattr(args, "all_data")
    assert args.user == getpass.getuser()
    assert not hasattr(args, "destination_folder")
    assert args.file_adapter == "csv"
    assert args.from_file == from_file


def test_user_flag_export(export_mode):
    user = getpass.getuser()
    args = parse_args(["-u", user, export_mode])
    assert args.mode == export_mode
    assert args.user == user


def test_user_flag_import(import_mode, from_file):
    user = getpass.getuser()
    args = parse_args(["-u", user, import_mode, "-f", from_file])
    assert args.mode == import_mode
    assert args.user == user


def test_file_adapter_flag_export(export_mode):
    file_adapter = export_mode
    args = parse_args(["-i", file_adapter, export_mode])
    assert args.mode == export_mode
    assert args.file_adapter == file_adapter


def test_file_adapter_flag_import(import_mode, from_file):
    file_adapter = "json"
    args = parse_args(["-i", file_adapter, import_mode, "-f", from_file])
    assert args.mode == import_mode
    assert file_adapter == file_adapter


def test_export_all_data_flag(export_mode):
    args = parse_args([export_mode, "-a"])
    assert args.mode == export_mode
    assert args.all_data


def test_export_destination_folder_flag(export_mode):
    destination_folder = "test "
    args = parse_args([export_mode, "-d", destination_folder])
    assert args.mode == export_mode
    assert args.destination_folder == destination_folder
