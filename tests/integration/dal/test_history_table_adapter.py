from chpass.dal.models.history import History


def test_get_history(chrome_db_adapter):
    history = chrome_db_adapter.history_db.history_table.get_chrome_history()
    assert all(isinstance(history_row, History) for history_row in history)


def test_get_history_serializable(chrome_db_adapter):
    history = chrome_db_adapter.history_db.history_table.get_chrome_history(serializable=True)
    assert all(isinstance(history_row, dict) for history_row in history)
