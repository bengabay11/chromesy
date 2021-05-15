import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from chpass.dal.models.login import Login
from chpass.exceptions.login_not_found_exception import LoginNotFoundException


@pytest.fixture(scope="module")
def invalid_login() -> int:
    return -1


@pytest.fixture(scope="module")
def login() -> dict:
    return {
        "origin_url": "test",
        "action_url": "test",
        "username_element": "test",
        "username_value": "test",
        "password_element": "test",
        "password_value": bytes(),
        "submit_element": "test",
        "signon_realm": "test",
        "date_created": 0,
        "blacklisted_by_user": 0,
        "scheme": 0,
        "password_type": 0,
        "times_used": 0,
        "form_data": bytes(),
        "date_synced": 0,
        "display_name": "test",
        "icon_url": "test",
        "federation_url": "test",
        "skip_zero_click": 0,
        "generation_upload_status": 0,
        "possible_username_pairs": bytes(),
        "date_last_used": 0,

    }


@pytest.fixture(scope="module")
def login_id_not_exist() -> int:
    return -1


@pytest.fixture(scope="module")
def invalid_login_id() -> str:
    return "invalid"


def test_get_logins(chrome_db_adapter):
    logins = chrome_db_adapter.logins_db.logins_table.get_all_logins()
    assert all(isinstance(login, Login) for login in logins)


def test_get_logins_serializable(chrome_db_adapter):
    logins = chrome_db_adapter.logins_db.logins_table.get_all_logins(serializable=True)
    assert all(isinstance(login, dict) for login in logins)


def test_insert_login(chrome_db_adapter, login):
    db_logins = chrome_db_adapter.logins_db.logins_table.get_all_logins()
    db_login_ids = [db_login.id for db_login in db_logins]
    login["id"] = max(db_login_ids) + 1
    chrome_db_adapter.logins_db.logins_table.insert_login(login)
    updated_db_logins = chrome_db_adapter.logins_db.logins_table.get_all_logins(serializable=True)
    assert login in updated_db_logins


def test_insert_invalid_login(chrome_db_adapter, invalid_login):
    with pytest.raises(TypeError):
        chrome_db_adapter.logins_db.logins_table.insert_login(invalid_login)


def test_insert_exist_login(chrome_db_adapter, login):
    with pytest.raises(IntegrityError):
        chrome_db_adapter.logins_db.logins_table.insert_login(login)


def test_get_login(chrome_db_adapter):
    login = chrome_db_adapter.logins_db.logins_table.get_all_logins()[0]
    result = chrome_db_adapter.logins_db.logins_table.get_login(login.id)
    assert result == login


def test_get_invalid_login(chrome_db_adapter, invalid_login_id):
    with pytest.raises(LoginNotFoundException):
        chrome_db_adapter.logins_db.logins_table.get_login(invalid_login_id, serializable=True)


def test_get_login_not_exist(chrome_db_adapter, login_id_not_exist):
    with pytest.raises(LoginNotFoundException):
        chrome_db_adapter.logins_db.logins_table.get_login(login_id_not_exist, serializable=True)


def test_delete_invalid_login_id(chrome_db_adapter, invalid_login_id):
    with pytest.raises(NoResultFound):
        chrome_db_adapter.logins_db.logins_table.delete_login(invalid_login_id)


def test_delete_login_not_exist(chrome_db_adapter, login_id_not_exist):
    with pytest.raises(NoResultFound):
        chrome_db_adapter.logins_db.logins_table.delete_login(login_id_not_exist)


def test_delete_login(chrome_db_adapter):
    login_id = chrome_db_adapter.logins_db.logins_table.get_all_logins()[-1].id
    chrome_db_adapter.logins_db.logins_table.delete_login(login_id)
    test_delete_login_not_exist(chrome_db_adapter, login_id)
