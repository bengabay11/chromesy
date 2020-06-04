# chret
> pulls out information about a person using chrome

## Installing
```bash
$ pip install chret
```

## Usage
### python
```python
from chret import get_credentials
for site_credentials in get_credentials():
    print(site_credentials)
```

### terminal
```bash
$ chret --get-credentials --output=credentials.csv
```
