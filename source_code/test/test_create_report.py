import pytest
from source_code.business_logic.report.report import Report

def make_tesable(function):
    def wrapper(*args,**kwargs):
        try:
            return function()
        except BaseException:
            return False
    return wrapper
class Test_create_report:

    def test_max_lenght_path():
        path = "/home/pc_user/filenamedwdwfdwehfuoefhowhfsdhiuhviuehviushviuewqhfviuhewqipuhgbeuhwqvrbuoewqgbfuoewqyrcfbuhogqygbyuhgbqyfhgeyugcbqeuwydrgwycgvuwycevbquyhwgvbwuhdgvcuhdgvcquhdwvcuhdvbcuohwqvedbcuhqdvbcuqwvbcuhdqcbihqedrcbiqprjebnvciedskjcpkjamcnpkjndmcknsadcoknajdcnkjsdnc.txt"
        report = Report(path)
        report.create_report = make_tesable(report.create_report())
        assert report == True

        """"
         'ports': {'21/tcp': {'service': 'ftp',
                              'state': 'open',
                              'version': 'vsftpd 2.3.4'},
                   '22/tcp': {'service': 'ssh',
                              'state': 'open',
                              'version': 'OpenSSH 4.7p1 Debian 8ubuntu1'},
                   '23/tcp': {'service': 'telnet',
                              'state': 'open',
                              'version': 'Linux telnetd '},
                   '25/tcp': {'service': 'smtp',
                              'state': 'open',
                              'version': 'Postfix smtpd '},
                   '53/tcp': {'service': 'domain',
                              'state': 'open',
                              'version': 'ISC BIND 9.4.2'},
                   '80/tcp': {'service': 'http',
                              'state': 'open',
                              'version': 'Apache httpd 2.2.8'}},
         'status': 'up'},
         os': {'accuracy': '100', 'name': 'Linux 2.6.9 - 2.6.33'},
         {'Vulnerabilities': {'service': {'OpenSSH 4.7p1 Debian 8ubuntu1': []}}
         '"""

        """{'Vulnerabilities': {'service': {'vsftpd 2.3.4': [{'description': 'The '
                                                                  'vsf_filename_passes_filter '
                                                                  'function in '
                                                                  'ls.c in '
                                                                  'vsftpd '
                                                                  'before '
                                                                  '2.3.3 '
                                                                  'allows '
                                                                  'remote '
                                                                  'authenticated '
                                                                  'users to '
                                                                  'cause a '
                                                                  'denial of '
                                                                  'service '
                                                                  '(CPU '
                                                                  'consumption '
                                                                  'and process '
                                                                  'slot '
                                                                  'exhaustion) '
                                                                  'via crafted '
                                                                  'glob '
                                                                  'expressions '
                                                                  'in STAT '
                                                                  'commands in '
                                                                  'multiple '
                                                                  'FTP '
                                                                  'sessions, a '
                                                                  'different '
                                                                  'vulnerability '
                                                                  'than '
                                                                  'CVE-2010-2632.',
                                                   'id': 'CVE-2011-0762',
                                                   'resource': 'ftp://vsftpd.beasts.org/users/cevans/untar/vsftpd-2.3.4/Changelog'},
                                                  {'description': 'vsftpd '
                                                                  '2.3.4 '
                                                                  'downloaded '
                                                                  'between '
                                                                  '20110630 '
                                                                  'and '
                                                                  '20110703 '
                                                                  'contains a '
                                                                  'backdoor '
                                                                  'which opens '
                                                                  'a shell on '
                                                                  'port '
                                                                  '6200/tcp.',
                                                   'id': 'CVE-2011-2523',
                                                   'resource': 'http://packetstormsecurity.com/files/162145/vsftpd-2.3.4-Backdoor-Command-Execution.html'}]}},
 'os': {'accuracy': '100', 'name': 'Linux 2.6.9 - 2.6.33'},
 'ports': {'21/tcp': {'service': 'ftp',
                      'state': 'open',
                      'version': 'vsftpd 2.3.4'},
           '22/tcp': {'service': 'ssh',
                      'state': 'open',
                      'version': 'OpenSSH 4.7p1 Debian 8ubuntu1'},
           '23/tcp': {'service': 'telnet',
                      'state': 'open',
                      'version': 'Linux telnetd '},
           '25/tcp': {'service': 'smtp',
                      'state': 'open',
                      'version': 'Postfix smtpd '},
           '53/tcp': {'service': 'domain',
                      'state': 'open',
                      'version': 'ISC BIND 9.4.2'},
           '80/tcp': {'service': 'http',
                      'state': 'open',
                      'version': 'Apache httpd 2.2.8'}},
 'status': 'up'}"""