import os

from chromesy.dal.ChromeDBAdapter import ChromeDBAdapter
from chromesy.services.chrome import export_profile_picture
from chromesy.services.file_adapters import csv


def export_chrome_data(chrome_db_adapter: ChromeDBAdapter, user: str, destination_folder: str) -> None:
    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)
    credentials = chrome_db_adapter.logins.logins.get_chrome_credentials()
    csv.write(credentials, f"{destination_folder}/credentials.csv")
    history = chrome_db_adapter.history.history.get_chrome_history()
    csv.write(history, f"{destination_folder}/history.csv")
    downloads = chrome_db_adapter.history.downloads.get_chrome_downloads()
    csv.write(downloads, f"{destination_folder}/downloads.csv")
    top_sites = chrome_db_adapter.top_sites.top_sites.get_top_sites()
    csv.write(top_sites, f"{destination_folder}/top_sites.csv")
    export_profile_picture(user, f"{destination_folder}/profile.jpg")


def import_chrome_data(chrome_db_adapter: ChromeDBAdapter, user: str) -> None:
    pass
