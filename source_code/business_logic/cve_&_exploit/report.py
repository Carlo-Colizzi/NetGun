import os, json
from cve import cve

def remove_brackets_string_json(string: str) -> str:
    if string == ',' or string == '}':
        return "\n"
    elif string == ']' or string == "[" or string == "{":
        return " "
    else:
        return string


class report:
    path = "report.txt"

    def __init__(self):
        pass

        
    @classmethod(f)
    def create_report(cls, result: dict) :
        string = str(result)
        file = open(self.path, "w") 
        print(string)
        for character in string:
            file.write(remove_brackets_string_json(character))
		


report = report()
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
result = cve(versions)
report.create_report(result.search_cve())






