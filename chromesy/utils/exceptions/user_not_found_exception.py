

class UserNotFoundException(Exception):
    def __init__(self, user: str) -> None:
        self._user = user
        message = f"User not found - {user}"
        super().__init__(message)

    @property
    def user(self) -> str:
        return self._user

    @user.setter
    def user(self, new_user: str) -> None:
        self._user = new_user
