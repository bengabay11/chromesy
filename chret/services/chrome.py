import os

from chret.dal.db_client import DBClient


CHROME_WINDOWS_PATH = "AppData\\Local\\Google\\Chrome\\User Data\\Default"
LOGINS_FILE = "Login Data"
HISTORY_FILE = "History"
TOP_SITES_FILE = "Top Sites"
DB_PROTOCOL = "sqlite"

db = DBClient()


def get_chrome_user_folder(user="~"):
    home_directory = os.path.expanduser(user)
    return os.path.join(home_directory, CHROME_WINDOWS_PATH)


def get_chrome_history_path(user="~"): return os.path.join(get_chrome_user_folder(user), HISTORY_FILE)


def get_chrome_credentials(user="~"):
    login_path = os.path.join(get_chrome_user_folder(user), LOGINS_FILE)
    db.connect(DB_PROTOCOL, "/" + login_path)
    credentials = db.get_chrome_credentials()
    db.close()
    return credentials


def export_chrome_credentials(output_file):
    pass


def import_chrome_credentials(credentials):
    pass


def get_chrome_history(user="~"):
    history_path = os.path.join(get_chrome_user_folder(user), HISTORY_FILE)
    db.connect(DB_PROTOCOL, "/" + history_path)
    history = db.get_chrome_history()
    db.close()
    return history


def chrome_downloads(user="~"):
    history_path = os.path.join(get_chrome_user_folder(user), HISTORY_FILE)
    db.connect(DB_PROTOCOL, "/" + history_path)
    downloads = db.get_chrome_downloads()
    db.close()
    return downloads


def get_top_sites(user="~"):
    top_site_path = os.path.join(get_chrome_user_folder(user), TOP_SITES_FILE)
    db.connect(DB_PROTOCOL, "/" + top_site_path)
    top_sites = db.get_chrome_top_sites()
    db.close()
    return top_sites


def get_google_profile_picture():
    profile_picture_path = os.path.join(get_chrome_user_folder(), "Google Profile Picture.png")
    return open(profile_picture_path, "rb")

get_top_sites()