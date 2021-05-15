

class LoginNotFoundException(Exception):
    def __init__(self, login_id: int) -> None:
        self._login_id = login_id
        message = f"login with id {self._login_id} not found in the db"
        super().__init__(message)

    @property
    def login_id(self) -> int:
        return self._login_id

    @login_id.setter
    def login_id(self, new_login_id: int) -> None:
        self._login_id = new_login_id
