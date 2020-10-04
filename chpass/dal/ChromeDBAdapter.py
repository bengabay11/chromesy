from chpass.dal.db_adapters.HistoryDBAdapter import HistoryDBAdapter
from chpass.dal.db_adapters.LoginsDBAdapter import LoginsDBAdapter
from chpass.dal.db_adapters.TopSitesTableAdapter import TopSitesDBAdapter
from chpass.utils.SingletonMeta import SingletonMeta


class ChromeDBAdapter(metaclass=SingletonMeta):
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
    def logins(self) -> LoginsDBAdapter:
        return self._logins_db_adapter

    @property
    def history(self) -> HistoryDBAdapter:
        return self._history_db_adapter

    @property
    def top_sites(self) -> TopSitesDBAdapter:
        return self._top_sites_db_adaper

    def close(self) -> None:
        for db_adapter in [self._logins_db_adapter, self._history_db_adapter, self._top_sites_db_adaper]:
            db_adapter.close()
