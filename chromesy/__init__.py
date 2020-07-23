# -*- coding: utf-8 -*-
"""
    chret
    ~~~~~
    chret is a package for getting information about a person using chrome browser.
    :copyright: 2020 Ben Gabay
    :license: MIT, see LICENSE for more details.
"""

from chromesy import config
from chromesy.chrome import ChromeDataAdapter
from chromesy.file_adapters.json_adapter import JsonFileAdapter

json_file_adapter = JsonFileAdapter()
chrome_data_adapter = ChromeDataAdapter(json_file_adapter)
chrome_data_adapter.connect_dbs("~", config.DB_PROTOCOL)
