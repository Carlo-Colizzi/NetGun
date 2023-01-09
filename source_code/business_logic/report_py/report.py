from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import cm
from fpdf import FPDF, XPos, YPos
from pprint import pprint
from urllib.parse import urlparse


def add_headers_table_horizontal(headers: list, pdf: FPDF(), col_width, line_height: float, align_header, emphasize_headers: list, emphaize_header_color, emphaize_header_style):
    for i in range(len(headers)):
        datum = headers[i]
        if len(emphasize_headers) > 0: 
            if datum in emphasize_headers or emphasize_headers[0] == "*":
                pdf.set_text_color(emphaize_header_color)
                pdf.set_font(style=emphaize_header_style)
                pdf.multi_cell(col_width, line_height, datum.capitalize(), border=0, align=align_header,  new_x=XPos.RIGHT, new_y=YPos.TOP, max_line_height=pdf.font_size)
                pdf.set_text_color(0,0,0)
                pdf.set_font(style='Times')
            else:
                pdf.multi_cell(col_width, line_height, datum.capitalize(), border=0, align=align_header,  new_x=XPos.RIGHT, new_y=YPos.TOP, max_line_height=pdf.font_size)
        else:
            pdf.multi_cell(col_width, line_height, datum.capitalize(), border=0, align=align_header,  new_x=XPos.RIGHT, new_y=YPos.TOP, max_line_height=pdf.font_size)
    return pdf




def add_data_table_horizontal(data:list, pdf:FPDF(), col_width, line_height, align_data, emphasize_data: list, emphasize_data_color, emphasize_data_style):
    for row in data:
        for element in row:
            if len(emphasize_data) > 0:
                if element in emphasize_data or emphasize_data[0] == "*":
                    pdf.set_text_color(*emphasize_data_color)
                    pdf.set_font(emphasize_data_style)
                    pdf.multi_cell(col_width, line_height, element, border=0, align=align_data,  new_x=XPos.RIGHT, new_y=YPos.TOP, max_line_height=pdf.font_size)
                    pdf.set_text_color(0,0,0)
                    pdf.set_font("Times")
                else:
                    pdf.multi_cell(col_width, line_height, element, border=0, align=align_data,  new_x=XPos.RIGHT, new_y=YPos.TOP, max_line_height=pdf.font_size)

            else:
                pdf.multi_cell(col_width, line_height, element, border=0, align=align_data, new_x=XPos.RIGHT, new_y=YPos.TOP, max_line_height=pdf.font_size)
        
        pdf.ln(line_height)
    return pdf


def get_max_height(row: list()):
    """
    Return element's max_height in the list 
    """
    max = 0
    for element in row:
        element_lenght = len(element)
        if element_lenght> max:
            max = element_lenght
    return max


def add_data_table_vertical(data:list, pdf:FPDF(), col_width, line_height, align_data, emphasize_data, emphaize_data_color, emphaize_data_style, separator: list()):
    for row in data:
        max_lenght = get_max_height(row)
        for element in row:
            if len(emphasize_data) > 0:
                if element in emphasize_data or emphasize_data[0] == "*":
                    pdf.set_text_color(*emphasize_data_color)
                    pdf.set_font(emphasize_data_style)
                    pdf.multi_cell(col_width, line_height, element, border='T', align=align_data,  new_x=XPos.RIGHT, new_y=YPos.LAST, max_line_height=max_lenght)
                    pdf.set_text_color(0,0,0)
                    pdf.set_font("Times")
                else:
                    pdf.multi_cell(col_width, line_height, element, border='T', align=align_data,  new_x=XPos.RIGHT, new_y=YPos.LAST, max_line_height= max_lenght)
            else:
                pdf.multi_cell(col_width, line_height, element, border='T', align=align_data,  new_x=XPos.RIGHT, new_y=YPos.LAST, max_line_height=max_lenght)
        pdf.ln(line_height)
    return pdf


def get_indexes(check_string: str, table_data)-> list:
    """"
    Return list indexes inside the main list where the string is located 
    - check_string: this is the string that we want to search
    - table_data: the main list where we search the check_string      
    """
    indexes = []
    for index, list_data in enumerate(table_data):
        for i, value in enumerate(list_data):
            if value == check_string:
                indexes.append(index)

    return indexes


def draw_table_pdf(table_data: list, title="", title_size = 14, data_size = 10, align_data = 'L', align_header = 'L', emphasize_data=['*'], emphasize_headers=['*'], emphaize_header_color = (0,0,0), emphaize_data_color = (0, 0, 0), emphaize_header_style = "Times", emphaize_data_style = "Times", type_table = "horizontal", pdf  = None ):
    """
    This function draws a table in a pdf using this parameters:
    - table_data: 
                        this is the list which contains the element we want to print in pdf
    - title (optional): 
                        title of table
    - title_size: 
                        the font size for the title of table
    - align_data: 
                        align table data:
                        - L : left align
                        - C: center align
                        - R: right align
    - align_header:
                        align table header:
                        - L : left align
                        - C: center align
                        - R: right align
    - emphasize_data:
                        which data element are to be emphasized (list)
    - emphasize_header:
                        which header element are to be emphasized(list)
    - emphasize_header_color:
                        used to set font color of the header
    - emphasize_data_color:
                        used to set font color of the data
    - emphasize_header_style:
                        used to set font style of the header
    - emphasize_data_style:
                        used to set font style of the data
    - table_type:
                        used to draw a table vertical or horizontal in the pdf. Default horizontal
    """
    
    
    if pdf is None:
        pdf = FPDF()
    
     
    pdf.set_font("Times", size=title_size)
      
    default_style = pdf.font_style

    
    col_width = pdf.epw / len(table_data[0]) 

    line_height = pdf.font_size * 2.5

    pdf.set_x(pdf.l_margin)

    if title != "":
        pdf.multi_cell(0, line_height, title, border = 0, align='j', max_line_height = title_size, markdown=True)
        pdf.ln(1)
    

    pdf.set_font(size=data_size)


    y1 = pdf.get_y()
    x_left = pdf.get_x()
    x_right = x_left + pdf.epw

    if type_table == "horizontal":
        headers = table_data[0]
        data = table_data[1:]
        pdf = add_headers_table_horizontal(headers, pdf, col_width, line_height, align_header, emphasize_headers, emphaize_header_color, emphaize_header_style)
        x_right =pdf.get_x()
        pdf.ln(line_height)
        y2 = pdf.get_y()
        pdf.line(x_left, y1, x_right, y1)
        pdf.line(x_left, y2, x_right, y2)
        pdf = add_data_table_horizontal(data, pdf, col_width, line_height, align_data, emphasize_data,emphaize_data_color, emphaize_data_style)

    elif type_table == "vertical":
        pdf.line(x_left, y1, x_right, y1)
        separator = get_indexes("service", table_data)
        
        pdf = add_data_table_vertical(table_data, pdf, col_width, line_height, align_header, emphasize_headers, emphaize_header_color, emphaize_header_style, separator=separator)
        pdf.ln(line_height)


    y3 = pdf.get_y()
    pdf.line(x_left, y3, x_right, y3)
    return pdf



def create_table_horizontal(elements:dict, index_table: str ) -> list:
        table = []
        for key, values in elements.items():
            list_key = [index_table]
            if isinstance(values, dict):
                if len(table) == 0:
                    for inner_key in values.keys():
                        list_key.append(inner_key)
                    table.append(list_key)
                else:
                    list_value = [key]
                    for inner_values in values.values():
                        list_value.append(inner_values)
                    table.append(list_value)
            else:
                if len(table) == 0:
                    keys = elements.keys()
                    values = elements.values()
                    table.append(list(keys))
                    table.append(list(values))
        return table


def create_table_vertical(elements:dict, index_table: str) -> list:
        table = []
        for keys, values in elements.items():
            table.append([index_table, keys])
            if isinstance(values, dict):
                for value in values.values():
                    if isinstance(value, list):
                        for i in range(len(value)):
                            for key, val in value[i].items():
                                table.append([key, val])
                    else:
                        for key, val in value.items():
                            table.append([key, val])
            else:
                table.append([keys, values])
    
        return table   

class Report:
    file = "report.pdf"
    # Lists used to decide which table to create
    __VERTICAL_TABLE = ["service"]   
    __HORIZONTAL_TABLE = ["ports", "os"]

        
    def create_report(self, result_scan: dict, result_cve: dict()) :
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Times", size=30)

        #pdf.image("images/NetgunLogo13.jpeg")

        pdf.set_title("Report")
        pdf.set_author("NetGun")
        pdf.multi_cell(0, pdf.font_size * 2.5, "Report", border = 0, align='C', max_line_height=50,  markdown=True)
        pdf.set_font(size=10)

        titles = ["Scan Result", "OS Detection"]
        i = 0
        for key, values in result_scan.items():
            table_scan = Report.create_table(values, key)
            if table_scan != []:
                pdf = draw_table_pdf(table_data = table_scan, title=titles[i], title_size = 16, data_size = 12, align_data = 'L', align_header = 'L', emphasize_data=['open'], emphasize_headers=[], emphaize_header_color = (0,0,0), emphaize_data_color = (0,100,0), emphaize_header_style = "Times", emphaize_data_style = "Times", type_table = "horizontal", pdf = pdf)
                pdf.ln()
                i += 1


        for key, values in result_cve.items():
            pdf = draw_table_pdf(table_data = Report.create_table(values, key), title="CVE Result", title_size = 16, data_size = 12, align_data = 'L', align_header = 'L', emphasize_data=['open'], emphasize_headers=[], emphaize_header_color = (0,0,0), emphaize_data_color = (0,100,0), emphaize_header_style = "Times", emphaize_data_style = "Times", type_table = "vertical", pdf = pdf)
            pdf.ln()
            
            
    

        pdf.output("report_prova.pdf")

    

    
    @classmethod
    def create_table(cls, results: dict, key: str) -> list:
        table_tmp = []
        if key in Report.__VERTICAL_TABLE:
            table_tmp = (create_table_vertical(results, key))
        if key in Report.__HORIZONTAL_TABLE:
            table_tmp = (create_table_horizontal(results, key))
    
        return table_tmp



        


        


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
result ={'service': {'ISC BIND 9.4.2': {'vulnerabilities': [{'id': 'CVE-2008-0122',
                                                        'description': 'Off-by-one error in '
                                                        'the inet_network '
                                                        'function in libbind '
                                                        'in ISC BIND 9.4.2 and '
                                                        'earlier, as used in '
                                                        'libc in FreeBSD 6.2 '
                                                        'through '
                                                        '7.0-PRERELEASE, '
                                                        'allows '
                                                        'context-dependent '
                                                        'attackers to cause a '
                                                        'denial of service '
                                                        '(crash) and possibly '
                                                        'execute arbitrary '
                                                        'code via crafted '
                                                        'input that triggers '
                                                        'memory corruption.',
                                         'resource': 'http://lists.opensuse.org/opensuse-security-announce/2008-03/msg00004.html'},
                                        { 'id': 'CVE-2008-1447',
                                        'description': 'The DNS protocol, as '
                                                        'implemented in (1) '
                                                        'BIND 8 and 9 before '
                                                        '9.5.0-P1, 9.4.2-P1, '
                                                        'and 9.3.5-P1; (2) '
                                                        'Microsoft DNS in '
                                                        'Windows 2000 SP4, XP '
                                                        'SP2 and SP3, and '
                                                        'Server 2003 SP1 and '
                                                        'SP2; and other '
                                                        'implementations allow '
                                                        'remote attackers to '
                                                        'spoof DNS traffic via '
                                                        'a birthday attack '
                                                        'that uses '
                                                        'in-bailiwick '
                                                        'referrals to conduct '
                                                        'cache poisoning '
                                                        'against recursive '
                                                        'resolvers, related to '
                                                        'insufficient '
                                                        'randomness of DNS '
                                                        'transaction IDs and '
                                                        'source ports, aka '
                                                        '"DNS Insufficient '
                                                        'Socket Entropy '
                                                        'Vulnerability" or '
                                                        '"the Kaminsky bug."',
                                         'resource': 'ftp://ftp.netbsd.org/pub/NetBSD/security/advisories/NetBSD-SA2008-009.txt.asc'},
                                        {'id': 'CVE-2008-4163',
                                        'description': 'Unspecified '
                                                        'vulnerability in ISC '
                                                        'BIND 9.3.5-P2-W1, '
                                                        '9.4.2-P2-W1, and '
                                                        '9.5.0-P2-W1 on '
                                                        'Windows allows remote '
                                                        'attackers to cause a '
                                                        'denial of service '
                                                        '(UDP client handler '
                                                        'termination) via '
                                                        'unknown vectors.',
                                         'resource': 'http://marc.info/?l=bind-announce&m=122180244228376&w=2'}]},
'vsftpd 2.3.4': {'vulnerabilities': [{
                                                    'id': 'CVE-2011-0762', 
                                                    'description': 'The '
                                                      'vsf_filename_passes_filter '
                                                      'function in ls.c in '
                                                      'vsftpd before 2.3.3 '
                                                      'allows remote '
                                                      'authenticated users to '
                                                      'cause a denial of '
                                                      'service (CPU '
                                                      'consumption and process '
                                                      'slot exhaustion) via '
                                                      'crafted glob '
                                                      'expressions in STAT '
                                                      'commands in multiple '
                                                      'FTP sessions, a '
                                                      'different vulnerability '
                                                      'than CVE-2010-2632.',
                                       'resource': 'ftp://vsftpd.beasts.org/users/cevans/untar/vsftpd-2.3.4/Changelog'},
                                      {'id': 'CVE-2011-2523',
                                        'description':  'vsftpd 2.3.4 downloaded '
                                                      'between 20110630 and '
                                                      '20110703 contains a '
                                                      'backdoor which opens a '
                                                      'shell on port 6200/tcp.',
                                       'resource': 'http://packetstormsecurity.com/files/162145/vsftpd-2.3.4-Backdoor-Command-Execution.html'}]},
                                       'OpenSSH 4.7p1 Debian 8ubuntu1': {'vulnerabilities': []}}}

    
report.create_report(versions, result)






