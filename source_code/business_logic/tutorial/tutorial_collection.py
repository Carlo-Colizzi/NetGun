import xml.etree.ElementTree as ET
from source_code.business_logic.tutorial.tutorial import Tutorial

"""@author: Carlo Colizzi"""
class Tutorial_collection:
    """This class represents a collection of Tutorials (Helps)"""

    def __init__(self, tutorials_dict):
        self.tutorials_dict = tutorials_dict

    def print_toString(self):
        print("name ", self.name)
        print("description: ", self.description)

    @classmethod
    def parse_tutorials_from_file(cls, path):
        """Parse the tutorial contained in the specified file, returning a dictionary"""
        tree = ET.parse(path)
        root = tree.getroot()

        tutorials_dict = {}
        for sub_root in root:
            t = Tutorial()
            for child in sub_root:
                setattr(t, child.tag, child.text)
            t.name = sub_root.tag
            tutorials_dict[sub_root.tag] = t

        return tutorials_dict

    @classmethod
    def inizialize_object_from_file_xml(cls, path):
        """Uses the parse_tutorial_from_file(self, path) method, for create a new Tutorial_collection object"""
        dictionary = Tutorial_collection.parse_tutorials_from_file(path)
        return Tutorial_collection(dictionary)