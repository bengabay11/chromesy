import pytest
from sqlalchemy.exc import ArgumentError, NoSuchModuleError

from chpass.dal.DBConnection import DBConnection
from chpass.dal.models.Login import Login
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


@pytest.fixture(scope="module")
def login_row():
    params = {
        "id": 1
    }
    return Login(**params)


def test_db_connection(db_connection, db_protocol, db_file_path):
    db_connection.connect(db_protocol, db_file_path)
    db_connection.close()


@pytest.mark.parametrize("db_protocol", [-1])
@pytest.mark.parametrize("db_file_path", [-1, "not_exist"])
def test_db_connection_invalid_protocol(db_connection, db_protocol, db_file_path):
    with pytest.raises(ArgumentError):
        db_connection.connect(db_protocol, db_file_path)


def test_db_connection_protocol_not_exist(db_connection, db_protocol_not_exist, db_file_path):
    with pytest.raises(NoSuchModuleError):
        db_connection.connect(db_protocol_not_exist, db_file_path)
