

class ChromeNotInstalledException(Exception):
    def __init__(self, user):
        self._user = user
        message = f"chrome is not installed for the user - {user}"
        super().__init__(message)

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, new_user):
        self._user = new_user
