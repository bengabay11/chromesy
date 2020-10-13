import os

CHROME_FOLDER_OS_PATHS = {
    "win32": r"AppData\Local\Google\Chrome\User Data",
    "linux": ".config/google-chrome",
    "linux2": ".config/google-chrome",
    "darwin": "Library/Application Support/Google/Chrome"
}

LOGINS_DB_FILE_PATH = os.path.join("Default", "Login Data")
HISTORY_DB_FILE_PATH = os.path.join("Default", "History")
TOP_SITES_DB_FILE_PATH = os.path.join("Default", "Top Sites")
GOOGLE_PICTURE_FILE_PATH = os.path.join("Default", "Google Profile Picture.png")
LOCAL_STATE_FILE_PATH = "Local State"

DEFAULT_EXPORT_DESTINATION_FOLDER = "dist"
OUTPUT_FILE_PATHS = {
    "csv": {
        "passwords": "passwords.csv",
        "history": "history.csv",
        "downloads": "downloads.csv",
        "top_sites": "top_sites.csv",
    },
    "json": {
        "passwords": "passwords.json",
        "history": "history.json",
        "downloads": "downloads.json",
        "top_sites": "top_sites.json",
    }
}
OUTPUT_PROFILE_PICTURE_FILE = "profile.jpg"
DEFAULT_EXPORT_ALL_DATA = False
DEFAULT_EXPORT_DECRYPT_PASSWORDS = True
DEFAULT_IMPORT_ENCRYPT_PASSWORDS = True

DB_PROTOCOL = "sqlite"

DEFAULT_FILE_ADAPTER = "csv"
CSV_ADAPTER_ENCODING = "utf-8"
DEFAULT_USER = "~"

WRITE_FILE_MODE = "w"
READ_FILE_MODE = "r"

PASSWORDS_FILE_BYTES_COLUMNS = ["form_data", "password_value", "possible_username_pairs"]
