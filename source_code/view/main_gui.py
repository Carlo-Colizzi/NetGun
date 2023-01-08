from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import customtkinter
import screeninfo
import webbrowser as web
import os

# storage path
storage_path = os.path.join("../persistence/storage")

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # configuration window main
        self.title("NetGun")
        self.geometry(f"1300x700") #default geometry
        # self.geometry("{}x{}".format(mon_width, mon_height))
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=4)
        # color scheme
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("dark-blue")

        # variables
        color_option_variable = customtkinter.StringVar(value="System")
        ip_var = customtkinter.StringVar(value="IP address")
        port_var = customtkinter.StringVar(value="Port")
        tcp_udp_var = customtkinter.StringVar(value="TCP-UDP")
        scan_type_var = customtkinter.StringVar(value="Shallow")
        scan_aggro_var = customtkinter.StringVar(value="0")
        chechbox_welcome_var = customtkinter.StringVar(value="on")


        # functions for button and other widgets
        def options_settings():
            window_options = customtkinter.CTkToplevel()
            window_options.geometry(f"400x200")
            window_options.title("Options")

            def change_mode_appearence(new_mode):
                customtkinter.set_appearance_mode(new_mode)

            # frame options
            frame_options = customtkinter.CTkFrame(window_options, fg_color="transparent")
            frame_options.grid(pady=30, padx=30, sticky="nsew")
            frame_options.place(relx=0.5, rely=0.5, anchor="c")

            # color mode set
            color_mode_label = customtkinter.CTkLabel(master=frame_options, text="Color Mode:")
            color_mode_label.grid(row=0, column=0, sticky="w")

            appearence_mode = customtkinter.CTkOptionMenu(master=frame_options, corner_radius=4, values=["System", "Dark", "Light"], command=change_mode_appearence, variable=color_option_variable)
            appearence_mode.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        def manual_command():
            # welcome frame and window
            manual_window = customtkinter.CTkToplevel()
            manual_window.geometry(f"800x400")
            manual_window.title("MANUAL")
            manual_window.columnconfigure(0, weight=1)
            manual_window.rowconfigure(0, weight=1)

            manual_frame = customtkinter.CTkFrame(master=manual_window, fg_color="transparent")
            manual_frame.grid(padx=30, pady=30, sticky="nsew")
            manual_frame.place(relx=0.5, rely=0.5, anchor="center")
            manual_frame.columnconfigure(0, weight=1)
            manual_frame.rowconfigure(0, weight=1)

            manual_label = customtkinter.CTkTextbox(master=manual_frame, wrap="word", width=750, height=350)
            manual_label.grid(row=0, column=0, sticky="nsew")
            manual_label.insert("end", "anche un testo preso da json o config")
            manual_label.configure(state="disabled")

        def speed_test_button():
            speed_test_window = customtkinter.CTkToplevel()
            speed_test_window.geometry(f"600x400")
            speed_test_window.title("Speed Test")
            speed_test_window.columnconfigure(0, weight=1)
            speed_test_window.rowconfigure(0, weight=1)

            speed_test_frame = customtkinter.CTkFrame(master=speed_test_window)
            speed_test_frame.grid(row=0, padx=30, pady=30, sticky="n")

            # funcion to speedtest
            def start_speedtest():

                # progress bar starting
                progress_bar_speedtest.start()

                # all the codes should be there
                # just for debugging progress bar
                for i in range(0, 1000):
                    progress_bar_speedtest.update(i)
                    
                # sample code for speedtest and change in the label text
                # down_label.configure(text=download_speed + "Mbps")
                # up_label.configure(text=upload_speed + "Mbps")
                # pg_label.configure(text=ping_speed + "ms")

                progress_bar_speedtest.stop()

            # all labels with the default labels for download and other
            download_label = customtkinter.CTkLabel(master=speed_test_frame, text="Download:", font=customtkinter.CTkFont(size=25, weight="bold"))
            download_label.grid(row=0, column=0, sticky="nw", padx=10)

            down_label = customtkinter.CTkLabel(master=speed_test_frame, text="0")
            down_label.grid(row=0, column=1, sticky="ne", padx=10)

            upload_label = customtkinter.CTkLabel(master=speed_test_frame, text="Upload:", font=customtkinter.CTkFont(size=25, weight="bold"))
            upload_label.grid(row=1, column=0, sticky="nw", padx=10)

            up_label = customtkinter.CTkLabel(master=speed_test_frame, text="0")
            up_label.grid(row=1, column=1, sticky="ne", padx=10)

            ping_label = customtkinter.CTkLabel(master=speed_test_frame, text="Ping:", font=customtkinter.CTkFont(size=25, weight="bold"))
            ping_label.grid(row=2, column=0, sticky="nw", padx=10)

            pg_label = customtkinter.CTkLabel(master=speed_test_frame, text="0")
            pg_label.grid(row=2, column=1, sticky="ne", padx=10)

            # add an other frame to handle start button and progress bar
            start_frame = customtkinter.CTkFrame(master=speed_test_window)
            start_frame.grid(row=1, padx=30, pady=30, sticky="n")

            # button to start speedtest
            start_button = customtkinter.CTkButton(master=start_frame, text="Start", command=start_speedtest)
            start_button.grid(row=1, column=0, sticky="n", pady=10)

            # progress bar
            progress_bar_speedtest = customtkinter.CTkProgressBar(master=start_frame, mode="indeterminate")
            progress_bar_speedtest.grid(row=0, column=0, sticky="nsew", pady=10)


        def welcome_page_comm():
            # welcome frame and window
            welcome_window = customtkinter.CTkToplevel()
            welcome_window.geometry(f"600x500")
            welcome_window.title("Welcome to NetGun")

            frame_welcome = customtkinter.CTkFrame(master=welcome_window, fg_color="transparent")
            frame_welcome.grid(pady=30, padx=30, sticky="nsew")
            frame_welcome.place(relx=0.5, rely=0.5, anchor="c")

            # text box with label of welcome message
            welcome_label = customtkinter.CTkTextbox(master=frame_welcome, width=350, height=70, wrap="word")
            welcome_label.grid(row=0, sticky="w", pady=15)
            welcome_label.insert("end", "Benvenuto, questo è NetGun, il programma perfetto per esperti e non, in ambito di ethical hacking. Buon hack a tutti!")
            welcome_label.configure(state="disabled")

            # button to open the manuale in a toplevel window
            manual_button = customtkinter.CTkButton(master=frame_welcome, text="Manual", command=manual_command)
            manual_button.grid(row=1, sticky="nsew", pady=15)

            # button to open all links in the browser
            github_button = customtkinter.CTkButton(master=frame_welcome, text="Github", command=lambda: web.open("https://github.com/MyCr4ck/NetGun_Classe03", new=2))
            github_button.grid(row=2, sticky="nsew", pady=15)

            # button for speedtest internet connection
            speedtest_button = customtkinter.CTkButton(master=frame_welcome, text="SpeedTest Ookla", command=speed_test_button)
            speedtest_button.grid(row=3, sticky="nsew", pady=15)

            # chech box if you want to open at startup
            chechbox_welcome = customtkinter.CTkCheckBox(master=frame_welcome, text="Apri al prossimo avvio", variable=chechbox_welcome_var, onvalue="on", offvalue="off")
            chechbox_welcome.grid(row=4, sticky="sw", pady=50)

        def open_top_adv():
            # started window and frame
            adv_window = customtkinter.CTkToplevel()
            adv_window.geometry(f"500x300")
            adv_window.title("Advanced Options")

            adv_frame = customtkinter.CTkFrame(master=adv_window, fg_color="transparent")
            adv_frame.grid(row=0, pady=30, padx=30, sticky="nsew")
            adv_frame.place(relx=0.5, rely=0.5, anchor="c")
            
            
            opt1_var = customtkinter.StringVar()
            opt2_var = customtkinter.StringVar()
            opt3_var = customtkinter.StringVar()

            # all the options in examples for debugging purposes
            option1_check = customtkinter.CTkCheckBox(master=adv_frame, text="Example 1", variable=opt1_var, onvalue="Example 1")
            option1_check.grid(row=0, column=0, sticky="n", pady=10)

            option2_check = customtkinter.CTkCheckBox(master=adv_frame, text="Example 2", variable=opt2_var, onvalue="Example 2")
            option2_check.grid(row=1, column=0, sticky="n", pady=10)

            option3_check = customtkinter.CTkCheckBox(master=adv_frame, text="Example 3", variable=opt3_var, onvalue="Example 3")
            option3_check.grid(row=2, column=0, sticky="n", pady=10)

            # button to kill the window and store the variables
            kill_button = customtkinter.CTkButton(master=adv_frame, text="OK", command=lambda: kill_window(adv_window))
            kill_button.grid(row=3, sticky="se", padx=30, pady=30)
            
            def kill_window(top):
                # storing variables and printing for debugging
                global option_var_1 
                global option_var_2
                global option_var_3
                option_var_1 = opt1_var.get()
                option_var_2 = opt2_var.get()
                option_var_3 = opt3_var.get()

                print(option_var_1)
                print(option_var_2)
                print(option_var_3)

                top.destroy()

        # a debugging function in terminal
        def start_scan():
            print("Starting scan...")

            ip = ip_var.get()
            port = port_var.get()
            tcp_udp = tcp_udp_var.get()
            scan_type = scan_type_var.get()
            scan_aggro = scan_aggro_var.get()

            print("Ip: {}".format(ip))
            print("Port: {}".format(port))
            print("TCP/UDP: {}".format(tcp_udp))
            print("Type: {}".format(scan_type))
            print("Aggro: {}".format(scan_aggro))
            print("Advanced: {} {} {}".format(option_var_1, option_var_2, option_var_3))

            # initialize tree structure
            scan_tree = ttk.Treeview(self.tree_frame, height=10)
            
            # see if the tree was here before
            treeview_exists = False
            for widget in scan_tree.winfo_children():
                if isinstance(widget,ttk.Treeview):
                    treeview_exists = True
                    break

            if treeview_exists == True:
                for widget in scan_tree.winfo_children():
                    if isinstance(widget, ttk.Treeview):
                        widget.destroy()

            # set number columns
            scan_tree["columns"] = ("colonna1", "colonna2", "colonna3")

            scan_tree.heading("#0", text="PORT")
            scan_tree.heading("colonna1", text="Service")
            scan_tree.heading("colonna2", text="Version")
            scan_tree.heading("colonna3", text="State")

            # date examples
            data = {
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
            }
            
            # label scannning
            self.scan_verbose.grid(row=3, column=1, sticky="nw", pady=10)

            # let appear the progress bar and start
            self.scan_progress.grid(row=3, column=0, sticky="nw", pady=10)
            self.scan_progress.start()

            # codes to find data should be here
            # to update the verbose you need to change the label eveytime verbose change in the progress
            # for example: self.scan_verbose.configure(text=<the actual text you want to appear>)

            # adding elements to the treeview
            for name, values in data.items():
                # add single element to the treeview
                scan_tree.insert("", "end", text=name, values=(values['service'], values['version'], values['state']))

            # stopping the process and destroying it
            self.scan_progress.stop()
            self.scan_progress.destroy()
            self.scan_verbose.destroy()

            print("Scan finished.")

            # positioning the treeview when start scanning
            scan_tree.grid(row=0, column=0, sticky="nsew", pady=10)

            def cve_button_click():
                # takes the element in the table
                item_focus = scan_tree.focus()

                # takes name and version
                name_focus = scan_tree.item(item_focus, "text")
                version_focus = data[name]['version']

                # create a top level window
                top_cve = customtkinter.CTkToplevel()
                top_cve.geometry(f"900x700")
                top_cve.title(name_focus)

                frame_cve = customtkinter.CTkFrame(top_cve)
                frame_cve.grid(row=0, pady=30, padx=30, sticky="nsew")
                frame_cve.place(relx=0.5, rely=0.5, anchor="c")

            def more_button_click():
                item_focus = scan_tree.focus()

                # takes name and service
                name_focus = scan_tree.item(item_focus, "text")
                service_focus = data[name]['service']

                # create a top level window
                top_more = customtkinter.CTkToplevel()
                top_more.geometry(f"900x700")
                top_more.title("More")

            # more button
            more_button = customtkinter.CTkButton(master=self.tree_frame, text="More", command=more_button_click, font=customtkinter.CTkFont(size=20, weight="bold"))
            more_button.grid(row=2, column=0, sticky="sew", pady=10)

            # button to open the cve file
            cve_button = customtkinter.CTkButton(master=self.tree_frame,text="Open CVE", command=cve_button_click, font=customtkinter.CTkFont(size=20, weight="bold"))
            cve_button.grid(row=1, column=0, sticky="sew")

        def export_file():
            file=filedialog.asksaveasfilename(filetypes=[("text file","*.txt")],
                                        defaultextension='.txt',
                                        title='Export Report')
            fob = open(file, 'w')
            fob.write("Hello, world!")
            fob.close()

        # main frame with options and label
        self.main_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(sticky="nsew")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="c")

        # label
        self.main_frame_label = customtkinter.CTkLabel(self.main_frame, text="NetGun", font=customtkinter.CTkFont(size=40, weight="bold"))
        self.main_frame_label.grid(row=0, column=0, sticky="nw")

        # options button
        self.options_button = customtkinter.CTkButton(self.main_frame, text="Opt", command=options_settings, width=30, height=30)
        self.options_button.grid(row=0, column=1, sticky="e")

        # buttons and text in main
        # set the frame first in the center of main_frame
        self.center_frame = customtkinter.CTkFrame(self.main_frame, fg_color="transparent")
        self.center_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=20)

        '''Step through every column from the first column to the last column'''
        # placeholders entry
        self.ip_entry = customtkinter.CTkEntry(master=self.center_frame, placeholder_text="IP Address", textvariable=ip_var)
        self.ip_entry.grid(row=0, column=0, sticky="w", padx=10)

        self.port_entry = customtkinter.CTkEntry(master=self.center_frame, placeholder_text="Port", textvariable=port_var, width=90)
        self.port_entry.grid(row=0, column=1, sticky="w", padx=10)

        # option menus
        self.tcp_udp_option = customtkinter.CTkOptionMenu(master=self.center_frame, values=["TCP", "UDP"], variable=tcp_udp_var, width=100)
        self.tcp_udp_option.grid(row=0, column=2, sticky="w", padx=10)

        # advanced settings to top level with all check box
        self.type_adv_option = customtkinter.CTkButton(master=self.center_frame, text="Advanced", command=open_top_adv, width=100)
        self.type_adv_option.grid(row=0, column=3, sticky="w", padx=10)

        # other options menu
        self.scan_type_option = customtkinter.CTkOptionMenu(master=self.center_frame, values=["Shallow", "Deep"], variable=scan_type_var, width=100)
        self.scan_type_option.grid(row=0, column=4, sticky="w", padx=10)

        self.scan_aggro_option = customtkinter.CTkOptionMenu(master=self.center_frame, values=["0","1","2","3","4"], variable=scan_aggro_var, width=10)
        self.scan_aggro_option.grid(row=0, column=5, sticky="w", padx=10)

        # button scan
        self.scan_button = customtkinter.CTkButton(self.center_frame, text="Scan", width=70, height=25, command=start_scan)
        self.scan_button.grid(row=0, column=6, sticky="nsew", padx=10)
        
        # frame with a tree view for the table
        self.tree_frame = customtkinter.CTkFrame(self.main_frame, height=300)
        self.tree_frame.grid(row=2, column=0, sticky="nsew", padx=40, pady=20)

        # progress bar, implemented but not started yet
        self.scan_progress = customtkinter.CTkProgressBar(master=self.main_frame, mode="indeterminate")
        # the progress bar needs the label too
        self.scan_verbose = customtkinter.CTkLabel(master=self.main_frame, text="Scanning...")

        # report folder button
        self.report_button_folder = customtkinter.CTkButton(self.main_frame, text="Export Report", command=export_file)
        self.report_button_folder.grid(row=4, column=0, padx=10, pady=50, sticky="se")

        # welcome frame button on the bottom main frame
        self.welcome_button = customtkinter.CTkButton(self.main_frame, text="Wel", command=welcome_page_comm, width=30)
        self.welcome_button.grid(row=4, column=1, sticky="se", pady=50)


if __name__ == "__main__":
    # get the size of the first screen from screeninfo
    screens = screeninfo.get_monitors()
    first_monitor = screens[0]
    print(first_monitor)

    # let the variable get the size of the monitor
    global mon_width
    global mon_height
    mon_width = first_monitor.width
    mon_height = first_monitor.height

    # debug to see if the path exists
    print(storage_path)
    for item in os.listdir(storage_path):
        print(item)

    app = App()
    app.mainloop()        