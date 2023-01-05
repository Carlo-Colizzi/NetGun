import xml.etree.ElementTree as ET
from source_code.business_logic.testing_misconfigurations.misconfiguration import Misconfiguration

class Services_misconfigurations:

    def __int__(self, misconfigurations_dict):
        self.misconfigurations_dict = misconfigurations_dict

    @classmethod
    def parse_misconfigurations_from_file(self, path):
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

        self.misconfigurations_dict = service_dict

    @classmethod
    def inizialize_object_from_file_xml(cls, path):
        dictionary = Services_misconfigurations.parse_misconfigurations_from_file(path)
        return Services_misconfigurations(dictionary)