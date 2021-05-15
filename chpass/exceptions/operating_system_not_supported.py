

class OperatingSystemNotSupported(Exception):
    def __init__(self, operating_system: str) -> None:
        self._operating_system = operating_system
        message = f"operating system not supported - {operating_system}"
        super().__init__(message)

    @property
    def operating_system(self) -> str:
        return self._operating_system

    @operating_system.setter
    def operating_system(self, new_operating_system: str) -> None:
        self._operating_system = new_operating_system
