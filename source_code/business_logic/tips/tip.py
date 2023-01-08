import xml.etree.ElementTree as ET
from source_code.business_logic.testing_misconfigurations.misconfiguration import Misconfiguration
import pprint
class Tip:

    def __int__(self):
        pass

    def print_toString(self):
        """Print all the object's variable"""
        print("service: ",self.service)
        print("acronym: ", self.acronym)
        print("description: ",self.description)
        print("default_port: ",self.default_port)

    @classmethod
    def parse_tips_from_file(cls, path):
        """Parse the tips contained in the specified file, returning a dictionary"""
        tree = ET.parse(path)
        root = tree.getroot()

        service_dict = {}
        for service in root:
            t = Tip()
            for child in service:
                setattr(t, child.tag, child.text)
            t.service = service.tag
            service_dict[service.tag] = t

        return service_dict


if __name__ == "__main__":
    path = "/home/ducky/Desktop/tip.xml"
    tipsDict = Tip.parse_tips_from_file(path)
    pprint.pprint(tipsDict)
    for i in tipsDict:
        tipsDict[i].print_toString()
        print("\n")