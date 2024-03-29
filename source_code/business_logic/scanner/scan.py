import nmap
from pprint import pprint
from source_code.business_logic.scanner.target import Target
from source_code.business_logic.scanner.filter import Filter
"""@author: Carlo Colizzi"""
class Scan:
    """Class Manager of the scan functionality"""

    __MODES_SUPPORTED = {"SHALLOW": "","DEEP" : "-sV"}

    def __init__(self, target : Target = None, filter : filter = None, scan_mode : str = "SHALLOW"):
        assert scan_mode in Scan.__MODES_SUPPORTED, "Invalid Mode Selected. Use SHALLOW or DEEP"
        assert target is not None, "Target is not selected"
        assert filter is not None, "Filter is not selected"
        self.target = target
        self.filter = filter


        self.scan_mode = scan_mode
        self.filter.advanced_options = Scan.__MODES_SUPPORTED[scan_mode] + self.filter.advanced_options

    def start_scan(self) -> dict :
        """Start the scanner on the specified Target and using the specified Filters, with the selected mode"""
        try:
            nm = nmap.PortScanner()

            resoults = nm.scan(self.target.ip,self.target.ports_range,self.filter.advanced_options)

            if self.scan_mode == "SHALLOW":
                parsed_result = self.parse_resoult_shallow(resoults)
            elif self.scan_mode == "DEEP":
                parsed_result = self.parse_resoult_deep(resoults)

        except:
            raise Exception("Something went wrong while scanning")
        return parsed_result

    def parse_resoult_shallow(self, resoult : """nmap dict"""):
        """The basic results received by nmap library aren't what we looking for, so,
                this function parse the results, filtering the original dictionary"""
        new_resoult = {}
        new_resoult["ports"] = {}
        if self.target.ip in resoult["scan"]:
            new_resoult["status"] = resoult["scan"][self.target.ip]["status"]["state"]

            if new_resoult["status"] == "up":
                if self.filter.transport_protocol in resoult["scan"][self.target.ip]:
                    for p in resoult["scan"][self.target.ip][self.filter.transport_protocol]:
                        p_tmp = str(p) + "/" + self.filter.transport_protocol
                        new_resoult["ports"][p_tmp] = {}
                        if "state" in resoult["scan"][self.target.ip][self.filter.transport_protocol][p]:
                            new_resoult["ports"][p_tmp]["state"] = resoult["scan"][self.target.ip][self.filter.transport_protocol][p]["state"]
                        if "name" in resoult["scan"][self.target.ip][self.filter.transport_protocol][p]:
                            new_resoult["ports"][p_tmp]["service"] = resoult["scan"][self.target.ip][self.filter.transport_protocol][p]["name"]

                if "osmatch" in resoult["scan"][self.target.ip]:
                    if len(resoult["scan"][self.target.ip]["osmatch"]) == 1:
                        if "name" in resoult["scan"][self.target.ip]["osmatch"][0] and "accuracy" in \
                                resoult["scan"][self.target.ip]["osmatch"][0]:
                            new_resoult["os"] = {"name": resoult["scan"][self.target.ip]["osmatch"][0]["name"],
                                                 "accuracy": resoult["scan"][self.target.ip]["osmatch"][0]["accuracy"]}
        else:
            new_resoult["status"] = "down"

        return new_resoult

    def parse_resoult_deep(self, resoult : """nmap dict"""):
        """The basic results received by nmap library aren't what we looking for, so,
                this function parse the results, filtering the original dictionary"""
        new_resoult = {}
        new_resoult["ports"] = {}
        if self.target.ip in resoult["scan"]:
            new_resoult["status"] = resoult["scan"][self.target.ip]["status"]["state"]

            if new_resoult["status"] == "up":
                if self.filter.transport_protocol in resoult["scan"][self.target.ip]:
                    for p in resoult["scan"][self.target.ip][self.filter.transport_protocol]:
                        p_tmp = str(p) + "/" + self.filter.transport_protocol
                        new_resoult["ports"][p_tmp] = {}
                        if "state" in resoult["scan"][self.target.ip][self.filter.transport_protocol][p]:
                            new_resoult["ports"][p_tmp]["state"] = resoult["scan"][self.target.ip][self.filter.transport_protocol][p]["state"]
                        if "name" in resoult["scan"][self.target.ip][self.filter.transport_protocol][p]:
                            new_resoult["ports"][p_tmp]["service"] = resoult["scan"][self.target.ip][self.filter.transport_protocol][p]["name"]
                        if "product" in resoult["scan"][self.target.ip][self.filter.transport_protocol][p]:
                            new_resoult["ports"][p_tmp]["version"] = resoult["scan"][self.target.ip][self.filter.transport_protocol][p]["product"]
                        if "version" in resoult["scan"][self.target.ip][self.filter.transport_protocol][p]:
                            new_resoult["ports"][p_tmp]["version"] += " " + resoult["scan"][self.target.ip][self.filter.transport_protocol][p]["version"]

                if "osmatch" in resoult["scan"][self.target.ip]:
                    if len(resoult["scan"][self.target.ip]["osmatch"]) == 1:
                        if "name" in resoult["scan"][self.target.ip]["osmatch"][0] and "accuracy" in resoult["scan"][self.target.ip]["osmatch"][0]:
                            new_resoult["os"] = {"name": resoult["scan"][self.target.ip]["osmatch"][0]["name"], "accuracy": resoult["scan"][self.target.ip]["osmatch"][0]["accuracy"]}

        else:
            new_resoult["status"] = "down"

        return new_resoult

if __name__ == "__main__":
    t = Target("192.168.1.1","1-1024")
    f = Filter("tcp",["OS detection"],4,)

    s = Scan(t,f,"DEEP")

    resoult = s.start_scan()


    pprint(resoult)








