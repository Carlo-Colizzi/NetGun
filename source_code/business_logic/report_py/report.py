from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import cm
from fpdf import FPDF, XPos, YPos


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



def get_col_width(table_data, pdf):
    col_widths = []
    for col in range(len(table_data[0])): # for every row
        longest = 0 
        for row in range(len(table_data)):                
            cell_value = str(table_data[row][col])
            value_length = pdf.get_string_width(cell_value)
            if value_length > longest:
                longest = value_length
                col_widths.append(longest + 4) # add 4 for padding
    return pdf.epw / len(table_data[0]) 

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



def add_headers_table_vertical(header:list):
    pass


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


def draw_table_pdf(table_data: list, title="", title_size = 14, data_size = 10, align_data = 'L', align_header = 'L', emphasize_data=['*'], emphasize_headers=['*'], emphaize_header_color = (0,0,0), emphaize_data_color = (0, 0, 0), emphaize_header_style = "Times", emphaize_data_style = "Times", type_table = "horizontal", pdf  = None ):
    if pdf is None:
        pdf = FPDF()
        pdf.set_font("Times")
      
    default_style = pdf.font_style
    
    col_width = get_col_width(table_data, pdf)

    headers = table_data[0]
    data = table_data[1:]

    line_height = pdf.font_size * 2.5

    pdf.set_x(pdf.l_margin)

    if title != "":
        pdf.multi_cell(0, line_height, title, border = 0, align='j', max_line_height = title_size)
        pdf.ln(line_height - 5)
    
    pdf.set_font(size=data_size)

    y1 = pdf.get_y()
    x_left = pdf.get_x()
    x_right = x_left + pdf.epw

    if type_table == "horizontal":
       pdf = add_headers_table_horizontal(headers, pdf, col_width, line_height, align_header, emphasize_headers, emphaize_header_color, emphaize_header_style)
       x_right =pdf.get_x()
       pdf.ln(line_height)
       y2 = pdf.get_y()
       pdf.line(x_left, y1, x_right, y1)
       pdf.line(x_left, y2, x_right, y2)
       #adjusted_col_width = col_width[0]
       pdf = add_data_table_horizontal(data, pdf, col_width, line_height, align_data, emphasize_data,emphaize_data_color, emphaize_data_style)
    elif type_table == "vertical":
        pass

    y3 = pdf.get_y()
    pdf.line(x_left, y3, x_right, y3)



    
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
    __VERTICAL_TABLE = []   
    __HORIZONTAL_TABLE = ["ports", "services"]

        
    def create_report(self, result_scan: dict, result_cve) :
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Times", size=10)

        table_scan = Report.create_table(result_scan)
        table_cve = Report.create_table(result_cve)
        draw_table_pdf(table_data = table_scan, title="Scan Result", title_size = 14, data_size = 10, align_data = 'L', align_header = 'L', emphasize_data=['open'], emphasize_headers=[], emphaize_header_color = (0,0,0), emphaize_data_color = (0,255,0), emphaize_header_style = "Times", emphaize_data_style = "Times", type_table = "horizontal", pdf = pdf)
        pdf.ln()
        #
        #for cve in table_cve:
        #draw_table_pdf(table_data = table_cve,  data_size = 4, title = "Research CVE Results", cell_width='uneven', pdf=pdf)
        #pdf.ln()
    

        pdf.output("report_prova.pdf")

    

    
    @classmethod
    def create_table(cls, results: dict) -> Table:
        for key, values in results.items():
            if key in Report.__VERTICAL_TABLE:
                table_tmp = (create_table_vertical(values, key))
            elif key in Report.__HORIZONTAL_TABLE:
                table_tmp = create_table_horizontal(values, key)
    
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
              'OpenSSH 4.7p1 Debian 8ubuntu1': {'description': '',
                                                'id': '',
                                                'reference': ''},
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






