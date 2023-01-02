import os, json, requests
from bs4 import BeautifulSoup
from pprint import pprint


def get_elements_from_json(path: str) -> dict:
    with open(path) as file:
        dict = json.load(file)
    return dict

def remove_file(path: str):
    os.system("rm " + path)

def found_element_in_html(text_site:str, search_tag:str) -> bool:
    soup = BeautifulSoup(text_site, "html.parser")

    if soup.find_all(search_tag)is not None:
        return True
    
    return False

    
class cve:
    path = "./exploits_result.json"
    version: str
    results: dict

    def __init__(self, version: str):
        assert version is not None, "Version not exists"
        self.version = version
        os.system("searchsploit -u")

    def search_cve(self):
        command_line = "searchsploit -j " + self.version
        results = os.popen(command_line)
        pprint(results)
        #results = get_elements_from_json(self.path)
        #remove_file(self.path)
        for cve in results['RESULTS_EXPLOIT']:
            if cve["Codes"] != "":
                if cve.verified_cve(cve) is True:
                    pass
                    
                    

    @classmethod
    def verified_cve(cls, cve:dict) -> bool:
        if cve["Verified"] == "1":
            return True
        return False


version = "http"
cve_element = cve(version)
cve_element.search_cve()
