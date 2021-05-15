import getpass

import pytest


@pytest.fixture(scope="session")
def connected_user() -> str:
    return getpass.getuser()
