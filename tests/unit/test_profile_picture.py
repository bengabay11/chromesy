import os

import pytest

from chpass.exceptions.UserNotFoundException import UserNotFoundException
from chpass import export_profile_picture


@pytest.fixture(scope="module")
def correct_destination_path() -> str:
    return "test_profile_picture.jpg"


def test_export_profile_picture(connected_user, correct_destination_path):
    export_profile_picture(connected_user, correct_destination_path)
    assert os.path.exists(correct_destination_path)
    os.remove(correct_destination_path)


@pytest.fixture
def user_not_exist() -> str:
    return "not_exist"


def test_export_profile_picture_user_not_exist(user_not_exist, correct_destination_path):
    with pytest.raises(UserNotFoundException):
        export_profile_picture(user_not_exist, correct_destination_path)
    assert not os.path.exists(correct_destination_path)


@pytest.fixture
def invalid_user() -> int:
    return -1


def test_export_profile_picture_invalid_user(invalid_user, correct_destination_path):
    with pytest.raises(TypeError):
        export_profile_picture(invalid_user, correct_destination_path)
    assert not os.path.exists(correct_destination_path)


@pytest.fixture
def destination_path_not_exist() -> str:
    return "not_exist/test_profile_picture.jpg"


def test_export_profile_picture_destination_path_not_exist(connected_user, destination_path_not_exist):
    with pytest.raises(FileNotFoundError):
        export_profile_picture(connected_user, destination_path_not_exist)
    assert not os.path.exists(destination_path_not_exist)


@pytest.fixture
def invalid_destination_path() -> int:
    return -1


def test_export_profile_picture_invalid_destination_path(connected_user, invalid_destination_path):
    with pytest.raises(ValueError):
        export_profile_picture(connected_user, invalid_destination_path)
    assert not os.path.exists(invalid_destination_path)
