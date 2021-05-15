import pytest
from sqlalchemy.exc import ArgumentError, NoSuchModuleError

from chpass.dal.db_connection import DBConnection
from chpass.services.path import get_chrome_logins_path


@pytest.fixture(scope="module")
def db_connection() -> DBConnection:
    return DBConnection()


@pytest.fixture(scope="module")
def db_protocol() -> str:
    return "sqlite"


@pytest.fixture(scope="module")
def db_protocol_not_exist() -> str:
    return "not_exist"


@pytest.fixture(scope="module")
def db_file_path(connected_user) -> str:
    return get_chrome_logins_path(connected_user)


def test_db_connection_close_fail(db_connection):
    with pytest.raises(AttributeError):
        db_connection.close()


def test_db_connection_connect(db_connection, db_protocol, db_file_path):
    db_connection.connect(db_protocol, db_file_path)


@pytest.mark.parametrize("db_protocol", [-1])
@pytest.mark.parametrize("db_file_path", [-1, "not_exist"])
def test_db_connection_connect_invalid_protocol(db_connection, db_protocol, db_file_path):
    with pytest.raises(ArgumentError):
        db_connection.connect(db_protocol, db_file_path)


def test_db_connection_connect_protocol_not_exist(db_connection, db_protocol_not_exist, db_file_path):
    with pytest.raises(NoSuchModuleError):
        db_connection.connect(db_protocol_not_exist, db_file_path)


def test_db_connection_close(db_connection):
    db_connection.close()
