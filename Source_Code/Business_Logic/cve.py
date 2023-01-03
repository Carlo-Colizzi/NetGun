import  requests, json, time
from pprint import pprint
    
class cve:
    path = "https://services.nvd.nist.gov/rest/json/cves/2.0?"
    versions: dict
    results: {}

    def __init__(self, versions: dict):
        assert versions is not None, "Version not exists"
        self.versions = versions

    def search_cve(self) :
        i = 0
        results = {}
        if "cpe" in  self.versions:
            params = {"CPE": self.versions["CPE"] + "isVulnerable"}
            response_cpe = requests.get(self.path, params=params)
            results = cve.get_vulnerabilities(response_cpe.json(), self.versions["CPE"])
        for port, info in versions['ports'].items():
            if 'version' in info:
                params = {"keywordSearch":  info["version"]}
                response_versione = requests.get(self.path, params = params)
                if response_versione.status_code == 200:
                    data = response_versione.json()
                    vulnerabilities = cve.get_vulnerabilities(data, info["version"])
                    i += 1
                    results[i] = [vulnerabilities]
        return results

    @classmethod
    def get_vulnerabilities(cls, data: dict, version) -> dict:
        results = {"Version": version}
        for cve in data["vulnerabilities"]:
                results["id"] = cve["cve"]["id"]
                results["description"] = cve["cve"]["descriptions"]
                results["references"] = cve["cve"]["references"][:4]
        return results



versions = {
    'ports': {
        '21/tcp': {'service': 'ftp', 'version': 'vsftpd 2.3.4', 'state': 'open'},
        '22/tcp': {'service': 'ssh', 'version': 'OpenSSH 4.7p1 Debian 8ubuntu1', 'state': 'open'},
        '23/tcp': {'service': 'telnet', 'version': 'Linux telnetd ', 'state': 'open'},
        '25/tcp': {'service': 'smtp', 'version': 'Postfix smtpd ', 'state': 'open'},
        '53/tcp': {'service': 'domain', 'version': 'ISC BIND 9.4.2', 'state': 'open'},
        '80/tcp': {'service': 'http', 'version': 'Apache httpd 2.2.8', 'state': 'open'},
        '111/tcp': {'service': 'rpcbind', 'version': ' ', 'state': 'open'},
        '139/tcp': {'service': 'netbios-ssn', 'version': 'Samba smbd 3.X - 4.X', 'state': 'open'},
        '445/tcp': {'service': 'netbios-ssn', 'version': 'Samba smbd 3.X - 4.X', 'state': 'open'},
        '512/tcp': {'service': 'exec', 'version': ' ', 'state': 'open'},
        '513/tcp': {'service': 'login', 'version': 'OpenBSD or Solaris rlogind ', 'state': 'open'},
        '514/tcp': {'service': 'tcpwrapped', 'version': ' ', 'state': 'open'}
    },
    'status': 'up',
    'os': {'name': 'Linux 2.6.9 - 2.6.33', 'accuracy': '100'}
}
cve_element = cve(versions)
pprint(cve_element.search_cve())
