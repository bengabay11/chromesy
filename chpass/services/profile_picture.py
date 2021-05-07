import getpass
from shutil import copyfile

from chpass.services.path import get_chrome_profile_picture_path


def export_profile_picture(destination_path: str, user: str = getpass.getuser()) -> None:
    source_path = get_chrome_profile_picture_path(user)
    copyfile(source_path, destination_path)
