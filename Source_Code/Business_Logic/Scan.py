import nmap3, Target, Filter

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
        nmap = nmap3.Nmap()
        results = nmap.scan_top_ports("host", args=self.filter.advanced_options)
        return results

t = Target("192.168.1.1","1-1024")
f = Filter()

s = Scan(t,f)

result = s.start_scan()
print(result)





