from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle



# lists that are needed to decide what table creates
__VERTICAL_TABLE = ["services", "os"]   
__HORIZONTAL_TABLE = ["ports"]

def remove_brackets_string_json(string: str) -> str:
    if string == ',' or string == '}':
        return "\n"
    elif string == ']' or string == "[" or string == "{":
        return " "
    else:
        return string


def create_table_horizontal(elements:dict) :
    table = []
    for key, values in elements:
             table.append([key, values])
    return table


def create_table_vertical(elements:dict) :
    table = [] 
    keys = elements.keys()
    values = elements.values()
    table.append(keys)
    table.append(values)
    return table   

def create_table(results: dict) -> Table:
    table_tmp = []
    for element_result in results:
        if element_result in __VERTICAL_TABLE:
            table_tmp = create_table_vertical(element_result)
        elif element_result in __HORIZONTAL_TABLE:
            table_tmp = create_table_horizontal(element_result)
   
    return Table(table_tmp)


class report:
    file = "report.pdf"


        
    def create_report(self, result_scan: dict, result_cve) :
        pdf_file = SimpleDocTemplate(file, pagesize =letter)

        table_scan = create_table(results_scan)
        table_cve = create_table(results_cve)

        style_table = TableStyle([    ('ALIGN', (0,0), (-1,-1), 'LEFT'),    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),    ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),    ('FONTSIZE', (0,0), (-1,-1), 12),    ('BOTTOMPADDING', (0,0), (-1,-1), 12),])

        table_scan.setStyle(style_table)
        table_cve.setStyle(style_table)

        elements = [table_scan, table_cve]

        pdf_file.build(elements)



        


        


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






