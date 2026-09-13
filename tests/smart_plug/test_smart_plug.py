from enum import StrEnum

import pytest

from src.simulator.devices.device import Status


class TestSmartPlug:
    @pytest.mark.parametrize('expected_status', [Status.ON])
    def test_check_status_plug(self,
                               plug,
                               expected_status: StrEnum):

        assert plug.status == expected_status
