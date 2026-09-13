from abc import ABC, abstractmethod
from enum import StrEnum, IntEnum


class MotionStatus(IntEnum):
    MovementOn = 1
    MovementOff = 0

class StatusDevice(StrEnum):
    Disconnected = 'ON'
    Connected = 'OFF'

class Device(ABC):
    def __init__(self,
                 name: str,
                 device_id: int,
                 status: str,
                 created_by : str,
                 battery_level: int,
                 gateway: list[str],
                 generate_data: dict):

        self._name = name
        self._status = status
        self._device_id = device_id
        self._created_by = created_by
        self._battery_level = battery_level
        self._gateway = gateway
        self._generate_data = generate_data

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def status(self) -> str:
        pass

    @property
    @abstractmethod
    def device_id(self) -> int:
        pass

    @property
    @abstractmethod
    def created_by(self) -> str:
        pass

    @property
    @abstractmethod
    def battery_level(self) -> int:
        pass

    @property
    @abstractmethod
    def gateway(self):
        pass

    @property
    @abstractmethod
    def generate_data(self):
        pass

    def __str__(self) -> str:
        return self._name

    def __repr__(self) -> str:
        pass

    def __eq__(self, other):
        if isinstance(self.device_id, Device):
            return self.device_id == other.device_id
        return None

    def __len__(self):
        return self._gateway

if __name__ == '__name__':
    pass

