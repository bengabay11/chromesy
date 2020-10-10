# chpass
Import and Export passwords for Chrome 🔑

## Additional Features
- history
- google account profile picture
- downloads
- top visited sites

## Installing
```bash
$ pip install chpass
```
you can also clone the repo and install locally:
```bash
scripts/install.sh
```

## Usage
export the user passwords:
```bash
chpass export
```
the file will be saved under `dist/passwords.csv`

import the passwords:
```bash
chpass import -f passwords.csv
```

## Requirements
- Python 3.6+
- Chrome 84.0+
- Windows 10/macOS/Linux

## License
This project is licensed under the terms of the MIT license.
