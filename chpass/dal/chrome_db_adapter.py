from pattern_singleton import Singleton

from chpass.dal.db_adapters.history_db_adapter import HistoryDBAdapter
from chpass.dal.db_adapters.logins_db_adapter import LoginsDBAdapter
from chpass.dal.db_adapters.top_sites_db_adapter import TopSitesDBAdapter


class ChromeDBAdapter(metaclass=Singleton):
    def __init__(
            self,
            logins_db_adapter: LoginsDBAdapter,
            history_db_adapter: HistoryDBAdapter,
            top_sites_db_adaper: TopSitesDBAdapter
    ):
        self._logins_db_adapter = logins_db_adapter
        self._history_db_adapter = history_db_adapter
        self._top_sites_db_adaper = top_sites_db_adaper

    @property
    def logins_db(self) -> LoginsDBAdapter:
        return self._logins_db_adapter

    @property
    def history_db(self) -> HistoryDBAdapter:
        return self._history_db_adapter

    @property
    def top_sites_db(self) -> TopSitesDBAdapter:
        return self._top_sites_db_adaper

    def close(self) -> None:
        for db_adapter in [self._logins_db_adapter, self._history_db_adapter, self._top_sites_db_adaper]:
            db_adapter.close()
