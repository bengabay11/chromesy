from shutil import copyfile

from chromesy.services.path import get_chrome_profile_picture_path


def export_profile_picture(user, destination_path):
    source_path = get_chrome_profile_picture_path(user)
    copyfile(source_path, destination_path)
