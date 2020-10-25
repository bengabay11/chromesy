import getpass

import pytest


@pytest.fixture(scope="session")
def connected_user() -> str:
    return getpass.getuser()


@pytest.fixture(scope="session")
def disconnected_user() -> str:
    return "Administrator"
