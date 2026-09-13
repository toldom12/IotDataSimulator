import pytest


class TestTemperatureSensors:
    def test_properties_constructor(self, sensor):
        assert sensor.name == 'BME280'
        assert  sensor.status == 'connected'
        assert sensor.device_id == 1
        assert sensor.created_by == 'mg'
    @pytest.mark.parametrize('battery_lvl',[-50, 100 ] )
    def test_battery_level(self,
                           battery_lvl,
                           sensor):

        sensor.battery_level = battery_lvl
        assert sensor.battery_level == 100





