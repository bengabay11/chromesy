import os

from chromesy.config import CHROME_WINDOWS_PATH, HISTORY_FILE, LOGINS_FILE, TOP_SITES_FILE, GOOGLE_PICTURE_FILE
from chromesy.utils.exceptions.chrome_not_installed_exception import ChromeNotInstalledException
from chromesy.utils.exceptions.user_not_found_exception import UserNotFoundException


def get_chrome_user_folder(user: str) -> str:
    home_directory = os.path.expanduser("~" + user)
    if not os.path.exists(home_directory):
        raise UserNotFoundException(user)
    chrome_user_folder = os.path.join(home_directory, CHROME_WINDOWS_PATH)
    if not os.path.exists(chrome_user_folder):
        raise ChromeNotInstalledException(user)
    return chrome_user_folder


def get_chrome_history_path(user: str) -> str:
    return "/" + os.path.join(get_chrome_user_folder(user), HISTORY_FILE)


def get_chrome_logins_path(user: str) -> str:
    return "/" + os.path.join(get_chrome_user_folder(user), LOGINS_FILE)


def get_chrome_top_sites_path(user: str) -> str:
    return "/" + os.path.join(get_chrome_user_folder(user), TOP_SITES_FILE)


def get_chrome_profile_picture_path(user: str) -> str:
    return os.path.join(get_chrome_user_folder(user), GOOGLE_PICTURE_FILE)
