import os


def export_chrome_data(chrome_data_adapter, user, destination_folder):
    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)
    chrome_data_adapter.export_credentials(f"{destination_folder}/credentials.csv")
    chrome_data_adapter.export_history(f"{destination_folder}/history.csv")
    chrome_data_adapter.export_profile_picture(user, f"{destination_folder}/profile.jpg")
    chrome_data_adapter.export_top_sites(f"{destination_folder}/top_sites.csv")
    chrome_data_adapter.export_downloads(f"{destination_folder}/downloads.csv")


def import_chrome_data(chrome_data_adapter, user):
    pass

