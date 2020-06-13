import os

from chret.dal.db_connection import DBConnection
from chret.dal.table_adapters.history import HistoryTableAdapter
from chret.dal.table_adapters.logins import LoginsTableAdapter
from chret.dal.table_adapters.top_sites import TopSitesTableAdapter

CHROME_WINDOWS_PATH = "AppData\\Local\\Google\\Chrome\\User Data\\Default"
LOGINS_FILE = "Login Data"
HISTORY_FILE = "History"
TOP_SITES_FILE = "Top Sites"
DB_PROTOCOL = "sqlite"

db = DBConnection()


def get_chrome_user_folder(user="~"):
    home_directory = os.path.expanduser(user)
    return os.path.join(home_directory, CHROME_WINDOWS_PATH)


def get_chrome_history_path(user="~"): return os.path.join(get_chrome_user_folder(user), HISTORY_FILE)


def get_chrome_credentials(user="~"):
    logins_table = LoginsTableAdapter(db)
    login_path = os.path.join(get_chrome_user_folder(user), LOGINS_FILE)
    db.connect(DB_PROTOCOL, "/" + login_path)
    credentials = logins_table.get_chrome_credentials()
    db.close()
    return credentials


def export_chrome_credentials(output_file):
    pass


def import_chrome_credentials(credentials):
    pass


def get_chrome_history(user="~"):
    history_table = HistoryTableAdapter(db)
    history_path = os.path.join(get_chrome_user_folder(user), HISTORY_FILE)
    db.connect(DB_PROTOCOL, "/" + history_path)
    history = history_table.get_chrome_history()
    db.close()
    return history


def chrome_downloads(user="~"):
    history_table = HistoryTableAdapter(db)
    history_path = os.path.join(get_chrome_user_folder(user), HISTORY_FILE)
    db.connect(DB_PROTOCOL, "/" + history_path)
    downloads = history_table.get_chrome_downloads()
    db.close()
    return downloads


def get_top_sites(user="~"):
    top_sites_table = TopSitesTableAdapter(db)
    top_site_path = os.path.join(get_chrome_user_folder(user), TOP_SITES_FILE)
    db.connect(DB_PROTOCOL, "/" + top_site_path)
    top_sites = top_sites_table.get_top_sites()
    db.close()
    return top_sites


def get_google_profile_picture():
    profile_picture_path = os.path.join(get_chrome_user_folder(), "Google Profile Picture.png")
    return open(profile_picture_path, "rb")

get_top_sites()