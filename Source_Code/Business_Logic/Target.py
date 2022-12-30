import re

class Target:

    def __init__(self, ip: str = "127.0.0.1", ports_range: str = "1-65535"):
        assert Target.check_ip(ip) == True, "Invalid IPv4 Address, check_ip(ip) failed"
        assert Target.check_ports(ports_range) == True, "Invalid Ports Range, check_ports(ports_range) failed"
        self.ip = ip
        self.ports_range = ports_range

    @classmethod
    def check_ip(cls, ip: str):
        pattern = "^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        if re.match(pattern, ip):
            return True
        return False

    @classmethod
    def check_ports(cls, ports:str):
        pattern = "^([0-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-5][0-9][0-9][0-9]|6[0-4][0-9][0-9]|65[0-4][0-9]|655[0-2])-(6553[0-5]|655[0-2][0-9]|65[0-4][0-9]|6[0-4][0-9][0-9]|[1-5][0-9][0-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9]|[0-9])$";
        if re.match(pattern, ports):
            values = ports.split("-", 1)
            if values[0] <= values[1]:
                return True
        return False
