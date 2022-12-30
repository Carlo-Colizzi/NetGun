import nmap3
from pprint import pprint
from Target import Target
from Filter import Filter

class Scan:
    __MODES_SUPPORTED = {"SHALLOW": "","DEEP" : "-sV -sC "}
    def __init__(self, target : Target = None, filter : Filter = None, scan_mode : str = "SHALLOW"):
        assert scan_mode in Scan.__MODES_SUPPORTED, "Invalid Mode Selected. Use SHALLOW or DEEP"
        assert target is not None, "Target is not selected"
        assert filter is not None, "Filter is not selected"
        self.target = target
        self.filter = filter
        self.scan_mode = scan_mode
        self.filter.advanced_options = Scan.__MODES_SUPPORTED[scan_mode] + self.filter.advanced_options


    def start_scan(self) -> dict :
        nm = nmap3.Nmap()
        resoults = nm.scan_top_ports(self.target.ip, args=self.filter.advanced_options + " -p " + self.target.ports_range)

        resoults = self.parseResoult(resoults)
        return resoults

    def parseResoult(self, resoult : """nmap dict"""):
        tmp_resoult = resoult[self.target.ip]["ports"]
        new_resoult = {}
        for r in tmp_resoult:
            del r["cpe"]
            del r["reason"]
            del r["reason_ttl"]
            r["service"] = r["service"]["name"]
            swap_id = r["portid"]
            del r["portid"]
            new_resoult[swap_id] = r

        return new_resoult




t = Target("192.168.1.1","1-1024")
f = Filter()

s = Scan(t,f)

resoult = s.start_scan()


pprint(resoult)








