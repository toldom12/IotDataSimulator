import json
import os
from enum import StrEnum, IntEnum, Enum
from typing import Optional

from generators.data_generator import DataGenerator
from simulator.devices.device import StatusDevice, MotionStatus


class MotionSensorGenerator(DataGenerator):
    def __init__(self):

        self._device_id: int = 0
        self._device_status: StrEnum = StatusDevice.Disconnected
        self.timestamp: int = 199999
        self.battery_status: int = 50
        self.motion_status: IntEnum = MotionStatus.MovementOff
        self.data : Optional[dict] = None

        self._file_path: Optional[str] = None

        dirname = str(os.path.dirname(__file__))
        logdir = os.path.join(dirname, "../data_logs")
        file_path = os.path.join(logdir, 'motion_sensor.json')
        self._file_path = file_path


    def generate_parameters_values(self):
        for i in range(1_000):
            yield {
                "device_id": self._device_id,
                "device_status": self._device_status,
                "battery_status": self.battery_status,
                "motion_status": self.motion_status,
                "timestamp" : self.timestamp
            }

    def generate_data(self):
        with open(f'{self._file_path}', 'w') as f:
            f.write("[")
            for d in self.generate_parameters_values():
                json.dump(d, f, indent=2)
                f.write(',\n')
            f.write("]")

if __name__ == '__main__':
    z =  MotionSensorGenerator()
    z.generate_data()

    pass

