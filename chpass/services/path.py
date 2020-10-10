import os
import sys

from chpass.config import (
    HISTORY_DB_FILE,
    LOGINS_DB_FILE,
    TOP_SITES_DB_FILE,
    GOOGLE_PICTURE_FILE,
    CHROME_FOLDER_OS_PATHS
)
from chpass.exceptions.ChromeNotInstalledException import ChromeNotInstalledException
from chpass.exceptions.OperatingSystemNotSupported import OperatingSystemNotSupported
from chpass.exceptions.UserNotFoundException import UserNotFoundException


def get_chrome_user_folder(user: str) -> str:
    home_directory = os.path.expanduser("~" + user)
    if not os.path.exists(home_directory):
        raise UserNotFoundException(user)
    if sys.platform not in CHROME_FOLDER_OS_PATHS.keys():
        raise OperatingSystemNotSupported(sys.platform)
    chrome_folder_path = CHROME_FOLDER_OS_PATHS[sys.platform]
    chrome_user_folder = os.path.join(home_directory, chrome_folder_path)
    if not os.path.exists(chrome_user_folder):
        raise ChromeNotInstalledException(user)
    return chrome_user_folder


def get_chrome_history_path(user: str) -> str:
    return "/" + os.path.join(get_chrome_user_folder(user), HISTORY_DB_FILE)


def get_chrome_logins_path(user: str) -> str:
    return "/" + os.path.join(get_chrome_user_folder(user), LOGINS_DB_FILE)


def get_chrome_top_sites_path(user: str) -> str:
    return "/" + os.path.join(get_chrome_user_folder(user), TOP_SITES_DB_FILE)


def get_chrome_profile_picture_path(user: str) -> str:
    return os.path.join(get_chrome_user_folder(user), GOOGLE_PICTURE_FILE)
