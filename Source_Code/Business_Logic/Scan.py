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
        if self.scan_mode == "SHALLOW":
            resoult = self.start_shallow_scan()
        else:
            resoult = self.start_deep_scan()

        return resoult

    def start_deep_scan(self):
        nm = nmap3.Nmap()
        resoults = nm.nmap_version_detection(self.target.ip,
                                             self.filter.advanced_options + " -p " + self.target.ports_range)

        if resoults.__contains__(self.target.ip):
            resoults = self.parse_resoult_deep(resoults)
            return resoults
        else:
            return {}

    def start_shallow_scan(self):
        nm = nmap3.Nmap()
        resoults = nm.nmap_stealth_scan(self.target.ip,
                                             self.filter.advanced_options + " -p " + self.target.ports_range)

        if resoults.__contains__(self.target.ip):
            resoults = self.parse_resoult_shallow(resoults)
            return resoults
        else:
            return {}

    def parse_resoult_shallow(self, resoult : """nmap dict"""):
        tmp_resoult = resoult[self.target.ip]["ports"]
        new_resoult = {}
        for r in tmp_resoult:
            if r.__contains__("cpe"):
                del r["cpe"]
            if r.__contains__("reason"):
                del r["reason"]
            if r.__contains__("reason_ttl"):
                del r["reason_ttl"]
            if r.__contains__("scripts"):
                del r["scripts"]
            if r.__contains__("service"):
                r["service"] = r["service"]["name"]

            if r.__contains__("portid"):
                swap_id = r["portid"]
                del r["portid"]

            new_resoult[swap_id] = r

        return new_resoult

    def parse_resoult_deep(self, resoult : """nmap dict"""):
        tmp_resoult = resoult[self.target.ip]["ports"]
        new_resoult = {}
        for r in tmp_resoult:
            if r.__contains__("cpe"):
                del r["cpe"]
            if r.__contains__("reason"):
                del r["reason"]
            if r.__contains__("reason_ttl"):
                del r["reason_ttl"]
            if r.__contains__("scripts"):
                del r["scripts"]
            if r.__contains__("service"):
                tmp = r["service"]
                r["service"] = tmp["name"]
                if tmp.__contains__("version") and tmp.__contains__("product"):
                    r["version"] = tmp["product"] + " " + tmp["version"]
                elif tmp.__contains__("version"):
                    r["version"] = tmp["version"]
                elif tmp.__contains__("product"):
                    r["product"] = tmp["product"]

            if r.__contains__("extrainfo"):
                r["extrainfo"] = tmp["extrainfo"]

            if r.__contains__("portid"):
                swap_id = r["portid"]
                del r["portid"]

            new_resoult[swap_id] = r

        return new_resoult



t = Target("192.168.1.1")
f = Filter()

s = Scan(t,f,"SHALLOW")

resoult = s.start_scan()


pprint(resoult)








