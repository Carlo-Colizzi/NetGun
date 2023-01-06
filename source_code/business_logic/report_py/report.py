from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


def remove_brackets_string_json(string: str) -> str:
    new_string = string.replace("{", "")
    new_string = new_string.replace("}", "")
    new_string = new_string.replace("'", "")
    return new_string
    

def create_table_horizontal(elements:dict, index_table: str ) -> list:
        table = []
        for key, values in elements.items():
            if len(table) == 0:
                list_key = [index_table]
                for inner_key in values.keys():
                    list_key.append(inner_key)
                table.append(list_key)
            else:
                list_value = [key]
                for inner_values in values.values():
                    list_value.append(inner_values)
                table.append(list_value)
        return table


def create_table_vertical(elements:dict, index_table: str) -> list:
        table = []
        for key, values in elements.items():
            table.append([key])
            for inner_key, inner_values in values.items():
                table.append([inner_key, inner_values])

        return table   

class Report:
    file = "report.pdf"
    # Lists used to decide which table to create
    __VERTICAL_TABLE = ["services"]   
    __HORIZONTAL_TABLE = ["ports"]

        
    def create_report(self, result_scan: dict, result_cve) :
        pdf_file = SimpleDocTemplate(self.file, pagesize =letter)

        table_scan = Report.create_table(result_scan)
        table_cve = Report.create_table(result_cve)

        style_table = TableStyle([    ('ALIGN', (0,0), (-1,-1), 'LEFT'),    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),    ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),    ('FONTSIZE', (0,0), (-1,-1), 12),    ('BOTTOMPADDING', (0,0), (-1,-1), 12),])

        table_scan.setStyle(style_table)
        table_cve.setStyle(style_table)

        elements = []
        elements.append(table_scan)
        elements.append(table_cve)

        pdf_file.build(elements)

    

    
    @classmethod
    def create_table(cls, results: dict) -> Table:
        table_tmp = []
        for key, values in results.items():
            if key in Report.__VERTICAL_TABLE:
                table_tmp.append(create_table_vertical(values, key))
            elif key in Report.__HORIZONTAL_TABLE:
                table_tmp.append(create_table_horizontal(values, key))
        return Table(table_tmp)



        


        


report = Report()
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
result = {'services': {'ISC BIND 9.4.2': {'description': 'Unspecified vulnerability in '
                                                'ISC BIND 9.3.5-P2-W1, '
                                                '9.4.2-P2-W1, and 9.5.0-P2-W1 '
                                                'on Windows allows remote '
                                                'attackers to cause a denial '
                                                'of service (UDP client '
                                                'handler termination) via '
                                                'unknown vectors.',
                                 'id': 'CVE-2008-4163',
                                 'reference': 'http://marc.info/?l=bind-announce&m=122180244228376&w=2'},
              'Linux telnetd ': {'description': 'telnetd in GNU Inetutils '
                                                'through 2.3, MIT krb5-appl '
                                                'through 1.0.3, and derivative '
                                                'works has a NULL pointer '
                                                'dereference via 0xff 0xf7 or '
                                                '0xff 0xf8. In a typical '
                                                'installation, the telnetd '
                                                'application would crash but '
                                                'the telnet service would '
                                                'remain available through '
                                                'inetd. However, if the '
                                                'telnetd application has many '
                                                'crashes within a short time '
                                                'interval, the telnet service '
                                                'would become unavailable '
                                                'after inetd logs a '
                                                '"telnet/tcp server failing '
                                                '(looping), service '
                                                'terminated" error. NOTE: MIT '
                                                'krb5-appl is not supported '
                                                'upstream but is shipped by a '
                                                'few Linux distributions. The '
                                                'affected code was removed '
                                                'from the supported MIT '
                                                'Kerberos 5 (aka krb5) product '
                                                'many years ago, at version '
                                                '1.8.',
                                 'id': 'CVE-2022-39028',
                                 'reference': 'https://git.hadrons.org/cgit/debian/pkgs/inetutils.git/commit/?id=113da8021710d871c7dd72d2a4d5615d42d64289'},
              'OpenSSH 4.7p1 Debian 8ubuntu1': {},
              'Postfix smtpd ': {'description': 'The STARTTLS implementation '
                                                'in qmail-smtpd.c in '
                                                'qmail-smtpd in the '
                                                'netqmail-1.06-tls patch for '
                                                'netqmail 1.06 does not '
                                                'properly restrict I/O '
                                                'buffering, which allows '
                                                'man-in-the-middle attackers '
                                                'to insert commands into '
                                                'encrypted SMTP sessions by '
                                                'sending a cleartext command '
                                                'that is processed after TLS '
                                                'is in place, related to a '
                                                '"plaintext command injection" '
                                                'attack, a similar issue to '
                                                'CVE-2011-0411.',
                                 'id': 'CVE-2011-1431',
                                 'reference': 'http://inoa.net/qmail-tls/vu555316.patch'},
              'vsftpd 2.3.4': {'description': 'vsftpd 2.3.4 downloaded between '
                                              '20110630 and 20110703 contains '
                                              'a backdoor which opens a shell '
                                              'on port 6200/tcp.',
                               'id': 'CVE-2011-2523',
                               'reference': 'http://packetstormsecurity.com/files/162145/vsftpd-2.3.4-Backdoor-Command-Execution.html'}}}
report.create_report(versions, result)






