import requests
from pprint import pprint


class Cve:
    path = "https://services.nvd.nist.gov/rest/json/cves/2.0?"
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " \
                            "(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    def __init__(self, versions: str):
        assert versions is not None, "Version not exists"
        self.versions = versions

    def search_cve(self) -> dict:
        """ Research CVE given a group of services from the Scan Result. 
        Return  a dictionary with Version, CVE-id, CVE description and resources where the user can read  """
        response_version = requests.get(self.path,
                                        params={"keywordSearch": self.versions},
                                        headers=self.header)
        try:
            if response_version.status_code == 200:
                data = response_version.json()
                results = Cve.get_vulnerabilities(data)
            else:
                raise Exception()
        except Exception as e:
            raise Exception("National Vulnerabilities Database not reachable")
        return results

    @classmethod
    def get_vulnerabilities(cls, data: dict) -> dict:
        """ Create a list of dictionary with Version, CVE-id, CVE Description e References"""
        results = []
        for cve in data["vulnerabilities"]:
            if len(cve["cve"]["references"]) > 0:
                results.append({"id": cve["cve"]["id"],
                                "description": cve["cve"]["descriptions"][0]["value"],
                                "resource": cve["cve"]["references"][0]["url"]})

        return results


cve_element = Cve("Apache httpd 2.2.8")
pprint(cve_element.search_cve())
