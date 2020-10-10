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

OUTPUT_CREDENTIALS_FILE = "passwords.csv"
OUTPUT_HISTORY_FILE = "history.csv"
OUTPUT_DOWNLOADS_FILE = "downloads.csv"
OUTPUT_TOP_SITES_FILE = "top_sites.csv"
OUTPUT_PROFILE_PICTURE_FILE = "profile.jpg"
DEFAULT_EXPORT_DESTINATION_FOLDER = "dist"
DEFAULT_EXPORT_ALL_DATA = False

DB_PROTOCOL = "sqlite"

CSV_ADAPTER_ENCODING = "utf-8"
DEFAULT_USER = "~"
WRITE_FILE_MODE = "w"

PASSWORDS_FILE_BYTES_COLUMNS = ["form_data", "password_value", "possible_username_pairs"]
