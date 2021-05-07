import pytest


@pytest.fixture(scope="module")
def export_mode() -> str:
    return "export"


@pytest.fixture(scope="module")
def file_adapter_type() -> str:
    return "json"


@pytest.fixture(scope="module")
def destination_folder() -> str:
    return "dist"


def test_default_export(export_mode):
    raise NotImplementedError


def test_export_with_connected_user(export_mode, connected_user):
    raise NotImplementedError


def test_export_with_disconnected_user(export_mode, disconnected_user):
    raise NotImplementedError


def test_export_file_adapter(export_mode, file_adapter_type):
    raise NotImplementedError


def test_export_destination_folder(export_mode, destination_folder):
    raise NotImplementedError
