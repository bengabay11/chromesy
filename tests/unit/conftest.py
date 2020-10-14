import getpass

import pytest

from chpass.dal.DBConnection import DBConnection


@pytest.fixture(scope="session")
def connected_user() -> str:
    return getpass.getuser()


@pytest.fixture(scope="session")
def db_connection() -> DBConnection:
    pass
