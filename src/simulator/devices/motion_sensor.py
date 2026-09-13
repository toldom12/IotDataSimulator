from src.simulator.devices.device import Device


class MotionSensor(Device):
    @property
    def name(self) -> str:
        return self._name

    @property
    def status(self) -> str:
        return self._status

    @property
    def device_id(self) -> int:
        return self._device_id

    @property
    def created_by(self) -> str:
        return self._created_by

    @property
    def battery_level(self) -> int:
        return self._battery_level

    @property
    def gateway(self) ->list[str]:
        return self._gateway

    @property
    def generate_data(self) -> dict:
        return self._generate_data
