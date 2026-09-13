import pytest

from src.simulator.devices.device import StatusDevice
from src.simulator.devices.smart_plug import SmartPlug




@pytest.fixture()
def plug():
    obj : SmartPlug = SmartPlug(name = 'SwitchHue',
                    device_id=2,
                    created_by='mg',
                    battery_level=100,
                    status=StatusDevice.Connected,
                    gateway=['255.224.223.222'],
                    generate_data={
                        'device_id': 2,
                        'serial_number': 9837327
                    })

    yield obj

    return None