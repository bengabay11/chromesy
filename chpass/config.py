CHROME_FOLDER_OS_PATHS = {
    "win32": r"AppData\Local\Google\Chrome\User Data\Default",
    "linux": ".config/google-chrome/Default/databases",
    "linux2": ".config/google-chrome/Default/databases",
    "darwin": "Library/Application Support/Google/Chrome"
}

LOGINS_DB_FILE = "Login Data"
HISTORY_DB_FILE = "History"
TOP_SITES_DB_FILE = "Top Sites"
GOOGLE_PICTURE_FILE = "Google Profile Picture.png"

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

DB_PROTOCOL = "sqlite"

DEFAULT_FILE_ADAPTER = "csv"
CSV_ADAPTER_ENCODING = "utf-8"
DEFAULT_USER = "~"
WRITE_FILE_MODE = "w"

PASSWORDS_FILE_BYTES_COLUMNS = ["form_data", "password_value", "possible_username_pairs"]
