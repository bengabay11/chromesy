# -*- coding: utf-8 -*-
"""
    chret
    ~~~~~
    chret is a package for getting information about a person using chrome browser.
    :copyright: 2020 Ben Gabay
    :license: MIT, see LICENSE for more details.
"""

from .chrome import import_chrome_credentials
from .chrome import export_chrome_credentials
from .chrome import get_chrome_history
from .chrome import get_google_profile_picture
from .chrome import get_chrome_downloads
from .chrome import get_top_sites
