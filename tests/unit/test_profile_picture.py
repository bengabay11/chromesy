import getpass
import os

import pytest

from chpass.exceptions.UserNotFoundException import UserNotFoundException
from chpass.services.profile_picture import export_profile_picture


@pytest.fixture(scope="module")
def correct_destination_path() -> str:
    return "test_profile_picture.jpg"


def test_export_profile_picture(correct_destination_path):
    user = getpass.getuser()
    export_profile_picture(user, correct_destination_path)
    assert os.path.exists(correct_destination_path)
    os.remove(correct_destination_path)


def test_export_profile_picture_user_not_exist(correct_destination_path):
    with pytest.raises(UserNotFoundException):
        user = "not_exist"
        export_profile_picture(user, correct_destination_path)
    assert not os.path.exists(correct_destination_path)


def test_export_profile_picture_invalid_user(correct_destination_path):
    with pytest.raises(TypeError):
        user = -1
        export_profile_picture(user, correct_destination_path)
    assert not os.path.exists(correct_destination_path)


def test_export_profile_picture_destination_path_not_exist():
    with pytest.raises(FileNotFoundError):
        user = getpass.getuser()
        destination_path = "not_exist/test_profile_picture.jpg"
        export_profile_picture(user, destination_path)
    assert not os.path.exists(destination_path)


def test_export_profile_picture_invalid_destination_path():
    with pytest.raises(ValueError):
        user = getpass.getuser()
        destination_path = -1
        export_profile_picture(user, destination_path)
    assert not os.path.exists(destination_path)
