import re

"""@author: Carlo Colizzi"""
class Target:
    """Class Manager of the scan Target"""

    def __init__(self, ip: str = "127.0.0.1", ports_range: str = "1-65535"):
        assert Target.check_ip(ip) == True, "Invalid IPv4 Address, use the IPv4 standard format please"
        assert Target.check_ports(ports_range) == True, "Invalid Ports Range, write in this way: \"FirstPort-LastPort\""
        self.ip = ip
        self.ports_range = ports_range

    @classmethod
    def check_ip(cls, ip: str):
        """Check if the ip is in the correct format for IPv4"""
        pattern = "^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        if re.match(pattern, ip):
            return True
        return False

    @classmethod
    def check_ports(cls, ports:str):
        """Check if the ports range is correct"""
        pattern = "^([0-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-5][0-9][0-9][0-9]|6[0-4][0-9][0-9]|65[0-4][0-9]|655[0-2])-(6553[0-5]|655[0-2][0-9]|65[0-4][0-9]|6[0-4][0-9][0-9]|[1-5][0-9][0-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9]|[0-9])$";
        if re.match(pattern, ports):
            values = ports.split("-", 1)
            if values[0] <= values[1]:
                return True
        return False
