from PIL import Image
from fpdf import FPDF, XPos, YPos
import os


def get_max_height(row: list()):
    """
    Return element's max_height in the list
    :param row: list of elements
    """
    max = 0
    for element in row:
        element_lenght = len(element)
        if element_lenght > max:
            max = element_lenght
    return max


class Report:
    # Lists used to decide which table to create
    __VERTICAL_TABLE = ["service"]
    __HORIZONTAL_TABLE = ["ports", "os"]

    def __init__(self, path=""):
        if path == "" or path == " ":
            self.path = "report.pdf"
        else:
            self.path = path

    def create_report(self, result_scan: dict):
        """
        create a report of scan results, cve search and os detection
        :param result_scan:  scan result which have to be written on a pdf
        :param result_cve: research cve result which have to be written on a pdf
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Times", size=30)

        icon_path = os.path.join("../persistence/storage/icons/")

        image_pdf = Image.open(os.path.join(icon_path, "netgun_logo.png"))

        pdf.image(image_pdf, x=90, w=50, h=50)

        pdf.set_title("Report")
        pdf.set_author("NetGun")
        pdf.multi_cell(0, pdf.font_size * 2.5, "Report", border=0, align='C', max_line_height=50, markdown=True)
        pdf.set_font(size=10)

        result_cve = result_scan["Vulnerabilities"]

        titles = ["Scan Result", "OS Detection"]
        i = 0
        for key, values in result_scan.items():
            table_scan = Report.create_table(values, key)
            if table_scan:
                pdf = Report.draw_table_pdf(table_data=table_scan, title=titles[i], title_size=16, data_size=12,
                                            align_data='C', align_header='C', emphasize_data=['open'],
                                            emphasize_headers=['ports', 'service', 'version', 'state', 'accuracy',
                                                               'name'],
                                            emphaize_header_color=(3, 0, 138), emphaize_data_color=(0, 100, 0),
                                            emphaize_header_style="Times", emphaize_data_style="Times",
                                            type_table="horizontal", pdf=pdf)
                pdf.ln()
                i += 1

        for key, values in result_cve.items():
            pdf = Report.draw_table_pdf(table_data=Report.create_table(values, key), title="CVE Result", title_size=16,
                                        data_size=12, align_data='L', align_header='L', emphasize_data=['open'],
                                        emphasize_headers=[], emphaize_header_color=(0, 0, 0),
                                        emphaize_data_color=(0, 100, 0),
                                        emphaize_header_style="Times", emphaize_data_style="Times",
                                        type_table="vertical",
                                        pdf=pdf)
            pdf.ln()

        pdf.output(self.path)

    @classmethod
    def create_table(cls, results: dict, key: str) -> list:
        """
        create horizontal or vertical table (change __VERTICAL_TABLE or __HORIZONTAL_TABLE if you want to create
        another table)
        :param results: elements you want to insert in a table
        :param key: value you want to insert into a table
        :return: a list as a table
        """
        table_tmp = []
        if key in Report.__VERTICAL_TABLE:
            table_tmp = (Report.create_vertical_table(results, key))
        if key in Report.__HORIZONTAL_TABLE:
            table_tmp = (Report.create_horizontal_table(results, key))

        return table_tmp

    @classmethod
    def create_vertical_table(cls, elements: dict, element: str) -> list:
        """
        Create a vertical table
        Key on the left and value on the right.
        :param elements: is a dictionary of elements that you want to save in the table
        :param element: is a element that you want to save and that is not within the dictionary
        :return: a list as a table
        """
        table = []
        for keys, values in elements.items():
            if len(values) > 0:
                if element:
                    table.append([element, keys])
                for index in range(len(values)):
                    for key, value in values[index].items():
                        table.append([key, value])
        return table

    @classmethod
    def create_horizontal_table(cls, elements: dict, index_table: str) -> list:
        """
        create a horizontal table.
        Keys on top and data below them.
        :param elements: is a dictionary of elements that you want to save in the table
        :param index_table: is a element that you want to save and that is not within the dictionary
        :return: a list as a table
        """
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

    @classmethod
    def draw_table_pdf(cls, table_data: list, title="", title_size=14, data_size=10, align_data='L', align_header='L',
                       emphasize_data=['*'], emphasize_headers=['*'], emphaize_header_color=(0, 0, 0),
                       emphaize_data_color=(0, 0, 0), emphaize_header_style="Times", emphaize_data_style="Times",
                       type_table="horizontal", pdf=None):

        """
        Draw a table in a pdf file
        :param table_data: list which contains the element we want to print in pdf.
        :param title: title of table. Default ''.
        :param title_size: the font size for the title of table. Default 14.
        :param data_size: the font size for the data of table. Default 10.
        :param align_data: align table data:
                            - L : left align
                            - C: center align
                            - R: right align
                            Default 'L'.
        :param align_header: align table header:
                            - L : left align
                            - C: center align
                            - R: right align
                            Default 'L'.
        :param emphasize_data:  which data  are to be emphasized (list). Default all data(*).
        :param emphasize_headers: which header are to be emphasized(list). Default all headers(*).
        :param emphaize_header_color: used to set font color of the header. Default (0, 0, 0)  = black.
        :param emphaize_data_color: used to set font color of the data. Default (0, 0, 0) = black.
        :param emphaize_header_style: used to set font style of the header. Default 'Times'.
        :param emphaize_data_style: used to set font style of the data. Default 'Times'.
        :param type_table: used to draw a table vertical or horizontal in the pdf. Default horizontal.
        :param pdf: used to draw in your pdf        :return:
        """
        if pdf is None:
            pdf = FPDF()

        pdf.set_font("Times", size=title_size)

        default_style = pdf.font_style

        col_width = pdf.epw / len(table_data[0])

        line_height = pdf.font_size * 2.5

        pdf.set_x(pdf.l_margin)

        if title != "":
            pdf.multi_cell(0, line_height, title, border=0, align='j', max_line_height=title_size, markdown=True)
            pdf.ln(1)

        pdf.set_font(size=data_size)

        y1 = pdf.get_y()
        x_left = pdf.get_x()
        x_right = x_left + pdf.epw

        if type_table == "horizontal":
            headers = table_data[0]
            data = table_data[1:]
            pdf = Report.add_horizontal_table_headers(headers, pdf, col_width, line_height, align_header,
                                                      emphasize_headers,
                                                      emphaize_header_color, emphaize_header_style)
            x_right = pdf.get_x()
            pdf.ln(line_height)
            y2 = pdf.get_y()
            pdf.line(x_left, y1, x_right, y1)
            pdf.line(x_left, y2, x_right, y2)
            pdf = Report.add_horizontal_table_data(data, pdf, col_width, line_height, align_data, emphasize_data,
                                                   emphaize_data_color, emphaize_data_style)

        elif type_table == "vertical":
            pdf.line(x_left, y1, x_right, y1)
            separator = Report.get_indexes("service", table_data)

            pdf = Report.add_vertical_table_data(table_data, pdf, col_width, line_height, align_header,
                                                 emphasize_headers,
                                                 emphaize_header_color, emphaize_header_style)
            pdf.ln(line_height)

        y3 = pdf.get_y()
        pdf.line(x_left, y3, x_right, y3)
        return pdf

    @classmethod
    def add_horizontal_table_headers(cls, headers: list, pdf: FPDF(), col_width, line_height: float, align_header,
                                     emphasize_headers: list, emphasize_header_color, emphasize_header_style) -> FPDF:
        """
        :param headers: header list used to save in table
        :param pdf: used to add the table
        :param col_width: column width
        :param line_height: line height
        :param align_header: align header:
                            - L : left align
                            - C: center align
                            - R: right align
        :param emphasize_headers: which header are to be emphasized(list)
        :param emphasize_header_color: used to set font color of the headers
        :param emphasize_header_style: used to set font style of the headers
        :return: pdf object
        """
        for i in range(len(headers)):
            datum = headers[i]
            if len(emphasize_headers) > 0:
                if datum in emphasize_headers or emphasize_headers[0] == "*":
                    pdf.set_text_color(*emphasize_header_color)
                    pdf.set_font(emphasize_header_style, size=15)
                    pdf.multi_cell(col_width, line_height, datum.capitalize(), border=0, align=align_header,
                                   new_x=XPos.RIGHT, new_y=YPos.TOP, max_line_height=pdf.font_size)
                    pdf.set_text_color(0, 0, 0)
                    pdf.set_font('Times', size=12)
                else:
                    pdf.multi_cell(col_width, line_height, datum.capitalize(), border=0, align=align_header,
                                   new_x=XPos.RIGHT, new_y=YPos.TOP, max_line_height=pdf.font_size)
            else:
                pdf.multi_cell(col_width, line_height, datum.capitalize(), border=0, align=align_header,
                               new_x=XPos.RIGHT,
                               new_y=YPos.TOP, max_line_height=pdf.font_size)
        return pdf

    @classmethod
    def add_horizontal_table_data(cls, data: list, pdf: FPDF(), col_width, line_height, align_data,
                                  emphasize_data: list,
                                  emphasize_data_color, emphasize_data_style):
        """
        Add data to pdf file
        :param data: data list used to save in table
        :param pdf: used to add the table
        :param col_width: column width
        :param line_height: line height
        :param align_data: align data:
                            - L : left align
                            - C: center align
                            - R: right align
        :param emphasize_data: which data are to be emphasized(list)
        :param emphasize_data_color: used to set font color of the data
        :param emphasize_data_style: used to set font style of the data
        :return: pdf object
        """
        for row in data:
            for element in row:
                if len(emphasize_data) > 0:
                    if element in emphasize_data or emphasize_data[0] == "*":
                        pdf.set_text_color(*emphasize_data_color)
                        pdf.set_font(emphasize_data_style)
                        pdf.multi_cell(col_width, line_height, element, border=0, align=align_data, new_x=XPos.RIGHT,
                                       new_y=YPos.TOP, max_line_height=pdf.font_size)
                        pdf.set_text_color(0, 0, 0)
                        pdf.set_font("Times")
                    else:
                        pdf.multi_cell(col_width, line_height, element, border=0, align=align_data, new_x=XPos.RIGHT,
                                       new_y=YPos.TOP, max_line_height=pdf.font_size)

                else:
                    pdf.multi_cell(col_width, line_height, element, border=0, align=align_data, new_x=XPos.RIGHT,
                                   new_y=YPos.TOP, max_line_height=pdf.font_size)

            pdf.ln(line_height)
        return pdf

    @classmethod
    def add_vertical_table_data(cls, data: list, pdf: FPDF(), col_width, line_height, align_data, emphasize_data,
                                emphasize_data_color, emphasize_data_style):
        """
        add data
        :param data: data list used to save in table
        :param pdf: used to add the table
        :param col_width: column width
        :param line_height: line height
        :param align_data: align data:
                            - L : left align
                            - C: center align
                            - R: right align
        :param emphasize_data: which data are to be emphasized(list)
        :param emphasize_data_color: used to set font color of the data
        :param emphasize_data_style: used to set font style of the data
        :return: pdf object
        """
        for row in data:
            max_lenght = get_max_height(row)
            for element in row:
                if len(emphasize_data) > 0:
                    if element in emphasize_data or emphasize_data[0] == "*":
                        pdf.set_text_color(*emphasize_data_color)
                        pdf.set_font(emphasize_data_style)
                        pdf.multi_cell(col_width, line_height, element, border='T', align=align_data, new_x=XPos.RIGHT,
                                       new_y=YPos.LAST, max_line_height=max_lenght)
                        pdf.set_text_color(0, 0, 0)
                        pdf.set_font("Times")
                    else:
                        pdf.multi_cell(col_width, line_height, element, border='T', align=align_data, new_x=XPos.RIGHT,
                                       new_y=YPos.LAST, max_line_height=max_lenght)
                else:
                    pdf.multi_cell(col_width, line_height, element, border='T', align=align_data, new_x=XPos.RIGHT,
                                   new_y=YPos.LAST, max_line_height=max_lenght)
            pdf.ln(line_height)
        return pdf

    @classmethod
    def get_indexes(cls, check_string: str, table_data) -> list:
        """"
        Return indexes list inside the main list where the string is located
        :param check_string: this is the string that we want to search
        :param table_data: the main list where we search the check_string
        :return: indexes list
        """
        indexes = []
        for index, list_data in enumerate(table_data):
            for i, value in enumerate(list_data):
                if value == check_string:
                    indexes.append(index)

        return indexes

"""
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
result = {'service': {'ISC BIND 9.4.2': [{'description': 'Off-by-one error in the inet_network '
                                                         'function in libbind in ISC BIND 9.4.2 and '
                                                         'earlier, as used in libc in FreeBSD 6.2 '
                                                         'through 7.0-PRERELEASE, allows '
                                                         'context-dependent attackers to cause a '
                                                         'denial of service (crash) and possibly '
                                                         'execute arbitrary code via crafted input '
                                                         'that triggers memory corruption.',
                                          'id': 'CVE-2008-0122',
                                          'resource': 'http://lists.opensuse.org/opensuse-security-announce/2008-03/msg00004.html'},
                                         {'description': 'The DNS protocol, as implemented in (1) '
                                                         'BIND 8 and 9 before 9.5.0-P1, 9.4.2-P1, '
                                                         'and 9.3.5-P1; (2) Microsoft DNS in '
                                                         'Windows 2000 SP4, XP SP2 and SP3, and '
                                                         'Server 2003 SP1 and SP2; and other '
                                                         'implementations allow remote attackers to '
                                                         'spoof DNS traffic via a birthday attack '
                                                         'that uses in-bailiwick referrals to '
                                                         'conduct cache poisoning against recursive '
                                                         'resolvers, related to insufficient '
                                                         'randomness of DNS transaction IDs and '
                                                         'source ports, aka "DNS Insufficient '
                                                         'Socket Entropy Vulnerability" or "the '
                                                         'Kaminsky bug."',
                                          'id': 'CVE-2008-1447',
                                          'resource': 'ftp://ftp.netbsd.org/pub/NetBSD/security/advisories/NetBSD-SA2008-009.txt.asc'},
                                         {'description': 'Unspecified vulnerability in ISC BIND '
                                                         '9.3.5-P2-W1, 9.4.2-P2-W1, and 9.5.0-P2-W1 '
                                                         'on Windows allows remote attackers to '
                                                         'cause a denial of service (UDP client '
                                                         'handler termination) via unknown vectors.',
                                          'id': 'CVE-2008-4163',
                                          'resource': 'http://marc.info/?l=bind-announce&m=122180244228376&w=2'}],
                      "Debian": []}}

report.create_report(versions, result)"""
