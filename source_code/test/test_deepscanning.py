import pytest

from source_code.business_logic.scanner.filter import Filter
from source_code.business_logic.scanner.scan import Scan
from source_code.business_logic.scanner.target import Target


class Test_deep_scanning:

    @pytest.mark.TC1_2_01
    def test_if_no_input(self):
        target = Target("192.168.1.198", "1-1024")
        filter = Filter()
        scan = Scan(target, filter)
        assert scan.scan_mode == "SHALLOW"

    @pytest.mark.TC1_2_02
    def test_if_input_deep(self):
        target = Target("192.168.1.198", "1-1024")
        filter = Filter()
        scan = Scan(target, filter,"DEEP")
        assert scan.scan_mode == "DEEP"
