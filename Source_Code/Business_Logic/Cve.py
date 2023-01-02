import os, json, requests
from bs4 import BeautifulSoup


def get_elements_from_json(path: str) -> dict:
    with open(path) as file:
        dict = json.load(file)
    return dict


def remove_file(path: str):
    os.system("rm " + path)


class Cve:
    path = "../exploits_result.json"
    version: str
    results: dict

    def __init__(self, version: str):
        assert version is not None, "Version not exists"
        self.version = version

    def search_cve(self):
        command_line = "searchsploit -u -j " + self.version + " >> " + self.path
        os.system(command_line)
        self.results = get_elements_from_json(self.path)
        remove_file(self.path)
        # print(self.results)
        for cve in self.results['RESULTS_EXPLOIT']:
            Cve.validate_cve(cve)

    @classmethod
    def validate_cve(cls, cve):
        header = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " \
                                "(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
        response = requests.get(cve['URL'], headers=header)
        print(response.url)


version = "http"
cve = Cve(version)
cve.search_cve()