import requests
from bs4 import BeautifulSoup


class Cve:
    # url to connect to exploitDB
    url = "https://www.exploit-db.com/search"

    version: str
    type: str
    platform: str
    port: int
    result: dict

    # Variable created because direct request with default user agent of python is blocked by firewall
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " \
                 "(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

    def __init__(self, version, type=None, platform=None, port=None):
        assert version is not None, "Version not exists"
        self.version = version
        self.type = type
        self.platform = platform
        self.port = None

    # searches verified CVEs with the service
    def search_cve(self) -> dict:
        params = "?q=" + self.version + "&verified=true"
        self.url += params

        if self.platform is not None:
            self.url += f"&platform={self.platform}"

        response = requests.get(self.url, headers={"User-Agent": self.USER_AGENT})
        data = response.content
        print(data)



version = input("Inserisci servizio:\n")
cve = Cve(version)
cve_dictionary = cve.search_cve()
print(cve_dictionary)
