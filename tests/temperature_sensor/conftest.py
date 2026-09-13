import pytest

from src.simulator.devices.temperature_sensor import TemperatureSensor


@pytest.fixture
def sensor():
    return  TemperatureSensor(name= 'BME280',
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

