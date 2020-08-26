import os

from chromesy import config


def get_chrome_user_folder(user=None):
    home_directory = os.path.expanduser(user)
    return os.path.join(home_directory, config.CHROME_WINDOWS_PATH)


def get_chrome_history_path(user=config.DEFAULT_USER):
    return "/" + os.path.join(get_chrome_user_folder(user), config.HISTORY_FILE)


def get_chrome_logins_path(user=config.DEFAULT_USER):
    return "/" + os.path.join(get_chrome_user_folder(user), config.LOGINS_FILE)


def get_chrome_top_sites_path(user=config.DEFAULT_USER):
    return "/" + os.path.join(get_chrome_user_folder(user), config.TOP_SITES_FILE)


def get_chrome_profile_picture_path(user=config.DEFAULT_USER):
    return os.path.join(get_chrome_user_folder(user), config.GOOGLE_PICTURE_FILE)
