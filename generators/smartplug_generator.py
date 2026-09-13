import json
import os

from typing import Optional

from generators.data_generator import DataGenerator
from simulator.devices.device import StatusDevice


class SmartPlugGenerator(DataGenerator):
    def __init__(self):
        dirname = str(os.path.dirname(__file__))
        logdir = os.path.join(dirname, "../data_logs")
        file_path = os.path.join(logdir, 'smartplug.json')
        self._file_path :str = file_path
        self._device_id: Optional[int] = 0
        self._vcc : Optional[int]= 230
        self._temperature: Optional[float] = 15.7
        self._humidity : Optional[float] = 45.5
        self._status: Optional[str]= StatusDevice.Disconnected
        self._data : Optional[dict] = None
        self._timestamp :Optional[int] = 1788964245


    def generate_parameters_value(self):
        for i in range(1_000):
            yield {
                "device_id": self._device_id + i,
                "vcc": self._vcc + 230,
                "temperature": self._temperature * i ,
                "humidity": self._humidity * i,
                "status": self._status,
                "timestamp": self._timestamp * i
            }

    def generate_data(self):
        with open(f'{self._file_path}', 'w') as f:
            f.write("[")
            for item in self.generate_parameters_value():
                    json.dump(item, f, indent=2)
                    f.write(",\n")
            f.write("]")


if __name__ == '__main__':
    A =SmartPlugGenerator()
    A.generate_data()

    pass




