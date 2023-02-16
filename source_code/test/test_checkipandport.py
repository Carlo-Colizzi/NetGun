import pytest
from source_code.business_logic.scanner.target import Target


"""Testing di unità"""
class Test_check_ip_and_port:

    @pytest.mark.TC1_1_01
    def test_long_ip_lenght(self):
        assert Target.check_ip("1.0-1.000000000000000000000") == False, "IP non rispetta la lunghezza"
        assert Target.check_ports("1-1024") == True, "Il range di porte non rispetta il formato"

    @pytest.mark.TC1_1_02
    def test_strange_ip_ports(self):
        assert Target.check_ip("192.168.1.100000000000000") == False, "IP non rispetta la lunghezza"
        assert Target.check_ports("43/655465") == False, "Il range di porte non rispetta il formato"

    @pytest.mark.TC1_1_03
    def test_normal_ip_ports(self):
        assert Target.check_ip("192.168.1.56") == True, "IP non rispetta la lunghezza"
        assert Target.check_ports("56-65535") == True, "Il range di porte non rispetta il formato"

    @pytest.mark.TC1_1_04
    def test_strange_ports_range(self):
        assert Target.check_ip("192.168.0.1") == True, "IP non rispetta la lunghezza"
        assert Target.check_ports("1*1024") == False, "Il range di porte non rispetta il formato"

    @pytest.mark.TC1_1_05
    def test_strange_ip_lenght(self):
        assert Target.check_ip("1939.0.1.020033.400.343") == False, "IP non rispetta la lunghezza"
        assert Target.check_ports("1-1024") == True, "Il range di porte non rispetta il formato"

    @pytest.mark.TC1_1_06
    def test_strange_everything(self):
        assert Target.check_ip("172-168,23-0000000") == False, "IP non rispetta la lunghezza"
        assert Target.check_ports("1/1024") == False, "Il range di porte non rispetta il formato"

    @pytest.mark.TC1_1_07
    def test_incorrect_format_ip(self):
        assert Target.check_ip("1.0.1.23-54") == False, "IP non rispetta la lunghezza"
        assert Target.check_ports("1-1024") == True, "Il range di porte non rispetta il formato"

    @pytest.mark.TC1_1_08
    def test_incorrect_everything(self):
        assert Target.check_ip("127-0-0-1") == False, "IP non rispetta la lunghezza"
        assert Target.check_ports("1004/0") == False, "Il range di porte non rispetta il formato"

