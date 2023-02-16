import pytest
from source_code.business_logic.scanner.target import Target


class test_checkipandport:

    def test_long_ip_lenght(self):
        assert Target.check_ip("1.0-1.000000000000000000000") == False, "IP non rispetta la lunghezza"
        assert Target.check_ports("1-1024") == True, "Il range di porte non rispetta il formato"

    def test_strange_ip_ports(self):
        assert Target.check_ip("192.168.1.100000000000000") == True, "IP non rispetta la lunghezza"
        assert Target.check_ports("43/655465") == True, "Il range di porte non rispetta il formato"

    def test_normal_ip_ports(self):
        assert Target.check_ip("192.168.1.56") == True, "IP non rispetta la lunghezza"
        assert Target.check_ports("56-65535") == True, "Il range di porte non rispetta il formato"

    def test_strange_ports_range(self):
        assert Target.check_ip("192.168.0.1") == True, "IP non rispetta la lunghezza"
        assert Target.check_ports("1*1024") == True, "Il range di porte non rispetta il formato"

    def test_strange_ip_lenght(self):
        assert Target.check_ip("1939.0.1.020033.400.343") == True, "IP non rispetta la lunghezza"
        assert Target.check_ports("1-1024") == True, "Il range di porte non rispetta il formato"


    def test_strange_everything(self):
        assert Target.check_ip("172-168,23-0000000") == True, "IP non rispetta la lunghezza"
        assert Target.check_ports("1/1024") == True, "Il range di porte non rispetta il formato"

    def test_incorrect_format_ip(self):
        assert Target.check_ip("1.0.1.23-54") == True, "IP non rispetta la lunghezza"
        assert Target.check_ports("1-1024") == True, "Il range di porte non rispetta il formato"

    def test_incorrect_everything(self):
        assert Target.check_ip("127-0-0-1") == True, "IP non rispetta la lunghezza"
        assert Target.check_ports("1004/0") == True, "Il range di porte non rispetta il formato"

