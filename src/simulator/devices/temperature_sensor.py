from abc import abstractmethod

from src.simulator.devices.device import Device

class RangeBatteryLevel(Exception):
    pass


class TemperatureSensor(Device):

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

    @battery_level.setter
    def battery_level(self,value: int):
        if value < 0 or value > 100:
            raise RangeBatteryLevel(f'[ERROR] Not expected value level {value}')
        else:
            self._battery_level = value


    @property
    def gateway(self) ->list[str]:
        return self._gateway
    @property
    def generate_data(self)-> dict:
        return self._generate_data



if __name__ == '__main__':
    t : Device = TemperatureSensor(name= 'BME280',
                                   status='connected',
                                   device_id=1,
                                   created_by='mg',
                                   battery_level=59,
                                   gateway=['255.255.255.1'],
                                   generate_data={
                                       'device_id': 1,
                                       'temperature': 23.6,
                                       'humidity':45.2
                                   })

    a = t.battery_level

    print(f'{a}')
