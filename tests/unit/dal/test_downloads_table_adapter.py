from chpass.dal.models.download import Download


def test_get_downloads(chrome_db_adapter):
    downloads = chrome_db_adapter.history_db.downloads_table.get_chrome_downloads()
    assert all(isinstance(download, Download) for download in downloads)


def test_get_downloads_serializable(chrome_db_adapter):
    downloads = chrome_db_adapter.history_db.downloads_table.get_chrome_downloads(serializable=True)
    assert all(isinstance(download, dict) for download in downloads)
