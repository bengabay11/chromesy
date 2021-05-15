from chpass.dal.models.topSite import TopSite


def test_get_top_sites(chrome_db_adapter):
    top_sites = chrome_db_adapter.top_sites_db.top_sites_table.get_top_sites()
    assert all(isinstance(top_site, TopSite) for top_site in top_sites)


def test_get_top_sites_serializable(chrome_db_adapter):
    top_sites = chrome_db_adapter.top_sites_db.top_sites_table.get_top_sites(serializable=True)
    assert all(isinstance(top_site, dict) for top_site in top_sites)
