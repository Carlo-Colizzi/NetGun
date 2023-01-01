import requests, json
from bs4 import BeautifulSoup


# function that replaces space with '%20' for create a valid URL
def replace_space_with_url_encode(url: str) -> str:
    return url.replace(" ", "%20")


def html_to_json(response):
    soup = BeautifulSoup(response.text, "html.parser")
    elements = soup.select("table.exploit_list tbody tr")
    for element in elements:
        print(element)


class Cve:
    # url to connect to exploitDB
    url = "https://www.exploit-db.com/search"

    version: str
    platform: str
    port: int
    result: dict

    # Variable created because direct request with default user agent of python is blocked by firewall
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " \
                 "(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

    def __init__(self, version, platform=None, port=None):
        assert version is not None, "Version not exists"
        self.version = version
        self.platform = platform
        self.port = port

    # searches verified CVEs with the service (and platform and port if exists)
    def search_cve(self) -> dict:
        params = f"?q=" + self.version
        self.url += params
        self.url = Cve.filter_searching_string(self.url, self.port, self.platform)
        self.url += "&verified=true"
        self.url = replace_space_with_url_encode(self.url)
        response = requests.get(self.url.lower(), headers={"User-Agent": self.USER_AGENT})
        print(self.url.lower())
        html_to_json(response)

        if response.status_code != 200:
            raise Exception(f"Error! Cannot reach ExploitDB server")

    # add filters to searching string
    @classmethod
    def filter_searching_string(cls, url, port=None, platform=None) -> str:
        if platform is not None:  # control if platform is not empty from scan result
            url += f"&platform={platform}"

        if port is not None:  # control if port number is not empty from scan result
            url += f"&port={port}"

        return url


version = "http apache"  # input("Inserisci servizio:\n")
platform = "Ruby"  # input("Inserisci Piattaforma:\n")
port = 80  # input("Inserisci porta:\n")
cve = Cve(version, platform, port)
cve_dictionary = cve.search_cve()
print(cve_dictionary)
