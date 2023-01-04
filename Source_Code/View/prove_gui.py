#from Source_Code.Business_Logic import scan
from Business_Logic.target import target 
#from Source_Code.Business_Logic.filter import filter
from main_gui import main

    def scan_start():
        ip_1 = ip_var.get()
        port_1 = port_var.get()
        '''tcp_udp_1 = tcp_udp_var.get().lower()
        type_adv_1 = type_adv_var.get()
        scan_type_1 = scan_type_var.get()'''

        t = target(ip_1, port_1)

        print(t)
            
scan_start()