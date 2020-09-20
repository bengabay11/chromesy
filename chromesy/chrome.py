import os

from chromesy.dal.ChromeDBAdapter import ChromeDBAdapter
from chromesy.interfaces.IFileAdapter import IFileAdapter
from chromesy.utils.chrome import export_profile_picture


def export_chrome_data(
        chrome_db_adapter: ChromeDBAdapter,
        file_adapter: IFileAdapter,
        user: str,
        destination_folder: str
) -> None:
    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)
    credentials = chrome_db_adapter.logins.logins.get_chrome_credentials()
    file_adapter.write(credentials, f"{destination_folder}/credentials.csv")
    history = chrome_db_adapter.history.history.get_chrome_history()
    file_adapter.write(history, f"{destination_folder}/history.csv")
    downloads = chrome_db_adapter.history.downloads.get_chrome_downloads()
    file_adapter.write(downloads, f"{destination_folder}/downloads.csv")
    top_sites = chrome_db_adapter.top_sites.top_sites.get_top_sites()
    file_adapter.write(top_sites, f"{destination_folder}/top_sites.csv")
    export_profile_picture(user, f"{destination_folder}/profile.jpg")


def import_chrome_data(chrome_db_adapter: ChromeDBAdapter, file_adapter: IFileAdapter, user: str) -> None:
    pass
