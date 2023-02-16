import pytest
from source_code.business_logic.scanner.scan import Scan


class Test_deep_scanning:

    @pytest.mark.TC1_2_01
    def test_if_no_input(self):
        scan = Scan("192.168.1.198", "1-1024", "")
        assert scan.start_scan() is  None

    @pytest.mark.TC1_2_02
    def test_if_input_deep(self):
        scan = Scan("192.168.1.198", "1-1024", "DEEP")
        assert scan.start_scan() is not None
