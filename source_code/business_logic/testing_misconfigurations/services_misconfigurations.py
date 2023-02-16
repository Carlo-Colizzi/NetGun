import xml.etree.ElementTree as ET
from source_code.business_logic.testing_misconfigurations.misconfiguration import Misconfiguration

class Services_misconfigurations:
    """This class represents a collection of misconfigurations"""

    def __init__(self, misconfigurations_dict):
        self.misconfigurations_dict = misconfigurations_dict

    @classmethod
    def parse_misconfigurations_from_file(cls, path):
        """Parse the misconfigurations contained in the specified file, returning a dictionary"""
        tree = ET.parse(path)
        root = tree.getroot()

        service_dict = {}
        for service in root:
            service_dict[service.tag] = []
            for misconfiguration in service:
                m = Misconfiguration()
                for child in misconfiguration:
                    setattr(m, child.tag, child.text)
                service_dict[service.tag].append(m)

        return service_dict

    @classmethod
    def inizialize_object_from_file_xml(cls, path):
        """Uses the parse_misconfigurations_from_file(self, path) method, for create a new Services_misconfigurations object"""
        dictionary = Services_misconfigurations.parse_misconfigurations_from_file(path)
        return Services_misconfigurations(dictionary)


if __name__ == "__main__":
    sm = Services_misconfigurations.inizialize_object_from_file_xml("/home/ducky/Desktop/misconfiguration.xml")
    ftp1 = sm.misconfigurations_dict["ftp"][0]
    print(ftp1.print_toString())
    ftp1.test_misconfiguration()
