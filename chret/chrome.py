import os

from . import config
from .csv import write_csv_file, read_csv_file
from .dal.db_connection import DBConnection
from .dal.table_adapters.history import HistoryTableAdapter
from .dal.table_adapters.logins import LoginsTableAdapter
from .dal.table_adapters.top_sites import TopSitesTableAdapter


db = DBConnection()


def get_chrome_user_folder(user=config.DEFAULT_USER):
    home_directory = os.path.expanduser(user)
    return os.path.join(home_directory, config.CHROME_WINDOWS_PATH)


def get_chrome_history_path(user=config.DEFAULT_USER):
    return os.path.join(get_chrome_user_folder(user), config.HISTORY_FILE)


def get_chrome_credentials(user=config.DEFAULT_USER):
    logins_table = LoginsTableAdapter(db)
    login_path = os.path.join(get_chrome_user_folder(user), config.LOGINS_FILE)
    db.connect(config.DB_PROTOCOL, "/" + login_path)
    credentials = logins_table.get_chrome_credentials()
    db.close()
    return credentials


def insert_chrome_credentials(credentials): pass


def export_chrome_credentials(output_file=config.DEFAULT_CREDENTIALS_FILE, user=config.DEFAULT_USER):
    credentials = get_chrome_credentials(user)
    write_csv_file(credentials, output_file)


def import_chrome_credentials(credentials_file=config.DEFAULT_CREDENTIALS_FILE):
    credentials = read_csv_file(credentials_file)
    insert_chrome_credentials(credentials)


def get_chrome_history(user=config.DEFAULT_USER):
    history_table = HistoryTableAdapter(db)
    history_path = os.path.join(get_chrome_user_folder(user), config.HISTORY_FILE)
    db.connect(config.DB_PROTOCOL, "/" + history_path)
    history = history_table.get_chrome_history()
    db.close()
    return history


def get_chrome_downloads(user=config.DEFAULT_USER):
    history_table = HistoryTableAdapter(db)
    history_path = os.path.join(get_chrome_user_folder(user), config.HISTORY_FILE)
    db.connect(config.DB_PROTOCOL, "/" + history_path)
    downloads = history_table.get_chrome_downloads()
    db.close()
    return downloads


def get_top_sites(user=config.DEFAULT_USER):
    top_sites_table = TopSitesTableAdapter(db)
    top_site_path = os.path.join(get_chrome_user_folder(user), config.TOP_SITES_FILE)
    db.connect(config.DB_PROTOCOL, "/" + top_site_path)
    top_sites = top_sites_table.get_top_sites()
    db.close()
    return top_sites


def get_google_profile_picture(user=config.DEFAULT_USER):
    profile_picture_path = os.path.join(get_chrome_user_folder(user), config.GOOGLE_PICTURE_FILE)
    return open(profile_picture_path, "rb")

get_top_sites()
