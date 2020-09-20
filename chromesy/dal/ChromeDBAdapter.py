from chromesy.utils.singleton_meta import SingletonMeta


class ChromeDBAdapter(metaclass=SingletonMeta):
    def __init__(self, logins_db_adapter, history_db_adapter, top_sites_db_adaper):
        self._logins_db_adapter = logins_db_adapter
        self._history_db_adapter = history_db_adapter
        self._top_sites_db_adaper = top_sites_db_adaper

    @property
    def logins(self):
        return self._logins_db_adapter

    @property
    def history_db_adapter(self):
        return self._history_db_adapter

    @property
    def top_sites_db_adaper(self):
        return self._top_sites_db_adaper
