import getpass
import os
import sys

import pytest

from chpass.exceptions.OperatingSystemNotSupported import OperatingSystemNotSupported
from chpass.exceptions.UserNotFoundException import UserNotFoundException
from chpass.services.path import get_home_directory, get_chrome_user_folder


def test_get_home_directory():
    user = getpass.getuser()
    home_directory = get_home_directory(user)
    assert os.path.basename(home_directory) == user
    assert os.path.exists(home_directory)


def test_get_home_directory_user_not_exist():
    user = "not_exist"
    with pytest.raises(UserNotFoundException):
        get_home_directory(user)


def test_get_home_directory_invalid_user():
    user = -1
    with pytest.raises(TypeError):
        get_home_directory(user)


def test_get_chrome_user_folder():
    user = getpass.getuser()
    chrome_user_folder = get_chrome_user_folder(user)
    assert os.path.exists(chrome_user_folder)


def test_get_chrome_user_folder_os_not_exist():
    sys.platform = "not_exist"
    user = getpass.getuser()
    with pytest.raises(OperatingSystemNotSupported):
        get_chrome_user_folder(user)


def test_get_chrome_user_folder_invalid_os():
    sys.platform = -1
    user = getpass.getuser()
    with pytest.raises(OperatingSystemNotSupported):
        get_chrome_user_folder(user)