from abc import abstractmethod

from src.simulator.devices.device import Device


class BatterySensor(Device):

    @abstractmethod
    def name(self) -> str:
        return self.name

    @abstractmethod
    def status(self)-> str:
        return self.status

    @abstractmethod
    def device_id(self)-> str:
        return self.device_id

    @abstractmethod
    def created_by(self)-> str:
        return self.created_by

    @abstractmethod
    def battery_level(self)-> str:
        return self.battery_level
