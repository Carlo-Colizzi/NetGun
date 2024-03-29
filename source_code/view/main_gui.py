import sys
from pprint import pprint
sys.path.insert(0, "../../../NetGun_Classe03")
from source_code.business_logic.cve.cve import Cve
from source_code.business_logic.scanner.filter import Filter
from source_code.business_logic.scanner.scan import Scan
from source_code.business_logic.scanner.target import Target
from source_code.business_logic.report.report import Report
from source_code.business_logic.testing_misconfigurations.misconfiguration import Misconfiguration
from source_code.business_logic.testing_misconfigurations.services_misconfigurations import Services_misconfigurations

import threading
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import customtkinter
import screeninfo
import webbrowser as web
import os
import configparser
from PIL import Image
from source_code.business_logic.test_network_performance.network_test import Network_test
from source_code.business_logic.application_context.context import Context
from source_code.business_logic.scanner import scan_result


"""@author: Antonio Mazzarella"""
class App(customtkinter.CTk):
    context = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        App.context = Context()
        App.context.start()
        App.context.option_var1 = ''
        App.context.option_var2 = ''
        App.context.option_var3 = ''
        App.context.option_var4 = ''


        storage_path = os.path.join("../persistence/storage")
        conf_path = os.path.join("../persistence/storage/config.ini")
        icon_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), ("../persistence/storage/icons"))

        # configuration window main
        self.title("NetGun")
        # self.geometry(f"1300x800")  # default geometry
        self.geometry("{}x{}".format(mon_width, mon_height))
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=4)

        # debug to see if the path exists
        print(storage_path)
        for item in os.listdir(storage_path):
            print(item)

        # load images
        self.logo_icon = customtkinter.CTkImage(Image.open(os.path.join(icon_path, "netgun_logo.png")), size=(100, 110))
        self.folder_icon = customtkinter.CTkImage(Image.open(os.path.join(icon_path, "folder_light.png")),
                                                  size=(25, 25))
        self.link_icon = customtkinter.CTkImage(Image.open(os.path.join(icon_path, "link_light.png")), size=(25, 25))
        self.option_icon = customtkinter.CTkImage(Image.open(os.path.join(icon_path, "option_light.png")),
                                                  size=(25, 25))
        self.profile_icon = customtkinter.CTkImage(Image.open(os.path.join(icon_path, "profile_light.png")),
                                                   size=(25, 25))
        self.save_icon = customtkinter.CTkImage(Image.open(os.path.join(icon_path, "save_light.png")), size=(25, 25))
        self.shortcut_icon = customtkinter.CTkImage(Image.open(os.path.join(icon_path, "shortcut_light.png")),
                                                    size=(25, 25))
        self.document_logo = customtkinter.CTkImage(Image.open(os.path.join(icon_path, "doc_light.png")), size=(25, 25))
        self.search_logo = customtkinter.CTkImage(Image.open(os.path.join(icon_path, "search_light.png")),
                                                  size=(25, 25))
        self.error_icon = customtkinter.CTkImage(Image.open(os.path.join(icon_path, "error_icon.png")), size=(20, 20))
        self.speedtest_logo = customtkinter.CTkImage(
            Image.open(os.path.join(icon_path, "Speedtest_Logo_July_2016.svg_.png")), size=(150, 150))

        # take the settings from configuration
        config = configparser.ConfigParser()
        config.read(conf_path)
        # set the default if the configuration file doesn't exist
        if os.path.exists(conf_path) == False:
            config.add_section('color_appearance')
            config["color_appearance"]["color_mode"] = "System"
            config.add_section('welcome')
            config["welcome"]["open_login"] = "on"

        system_color = config.get('color_appearance', 'color_mode')
        welcom_conf = config.get('welcome', 'open_login')

        # color scheme
        customtkinter.set_appearance_mode(system_color)
        customtkinter.set_default_color_theme("dark-blue")

        #variables
        color_option_variable = customtkinter.StringVar(value=system_color)
        ip_var = customtkinter.StringVar(value="127.0.0.1")
        port_var = customtkinter.StringVar(value="1-1024")
        tcp_udp_var = customtkinter.StringVar(value="TCP")
        scan_type_var = customtkinter.StringVar(value="DEEP")
        scan_aggro_var = customtkinter.StringVar(value="4")
        chechbox_welcome_var = customtkinter.StringVar(value=welcom_conf)
                
        # main button's dim variables
        main_font = customtkinter.CTkFont(size=18)
        main_width = 150
        main_height = 40
        quadr_width = 40
        quadr_height = 40

        def error_popup(exception):
            '''This is an error message, it shows an exception message taken with the error in given function'''
            top_error = customtkinter.CTkToplevel()
            top_error.geometry(f"800x100")
            top_error.title("Error")

            error_frame_main = customtkinter.CTkFrame(top_error)
            error_frame_main.grid(sticky="nsew")
            error_frame_main.place(relx=0.5, rely=0.5, anchor="c")

            text = " ERROR: " + str(exception)
            error_label = customtkinter.CTkLabel(master=error_frame_main, text=text,
                                                 image=self.error_icon, compound="left",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"), bg_color="#1a1a1a",
                                                 text_color="red")
            error_label.grid(sticky="nsew")
    
        # functions for button and other widgets
        def options_settings():
            '''Option settings popup, in this method you can change the color appearance and set it with save button'''
            window_options = customtkinter.CTkToplevel()
            window_options.geometry(f"400x200")
            window_options.title("Options")

            def change_mode_appearence(new_mode):
                customtkinter.set_appearance_mode(new_mode)

            def save_app_conf():
                app_var = color_option_variable.get()
                config = configparser.ConfigParser()

                config.read(conf_path)
                if config.has_section('color_appearance'):
                    config["color_appearance"]["color_mode"] = str(app_var)
                else:
                    config.add_section('color_appearance')
                    config["color_appearance"]["color_mode"] = str(app_var)

                with open(conf_path, 'w') as configfile:
                    config.write(configfile)

                window_options.destroy()

            # frame options
            frame_options = customtkinter.CTkFrame(window_options, fg_color="transparent")
            frame_options.grid(pady=30, padx=30, sticky="nsew")
            frame_options.place(relx=0.5, rely=0.5, anchor="c")

            # color mode set
            color_mode_label = customtkinter.CTkLabel(master=frame_options, text="Color Mode:",
                                                      font=customtkinter.CTkFont(size=18), )
            color_mode_label.grid(row=0, column=0, sticky="w")

            appearence_mode = customtkinter.CTkOptionMenu(master=frame_options, corner_radius=4,
                                                          values=["System", "Dark", "Light"],
                                                          command=change_mode_appearence,
                                                          variable=color_option_variable,
                                                          font=customtkinter.CTkFont(size=18))
            appearence_mode.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

            save_app_button = customtkinter.CTkButton(master=frame_options, text="Salva ", image=self.save_icon,
                                                      font=customtkinter.CTkFont(size=18), compound="right",
                                                      command=save_app_conf)
            save_app_button.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        def speed_test_button():
            '''Run a speedtest powered by Ookla in the nearest and better server'''
            speed_test_window = customtkinter.CTkToplevel()
            speed_test_window.geometry(f"600x400")
            speed_test_window.title("Speed Test")
            speed_test_window.columnconfigure(0, weight=1)
            speed_test_window.rowconfigure(0, weight=1)

            speed_test_frame = customtkinter.CTkFrame(master=speed_test_window, fg_color="transparent")
            speed_test_frame.grid(row=0, padx=30, pady=30, sticky="n")

            tmp_variable = 0
            lock = False

            # funcion to speedtest
            def start_speedtest():
                try:
                    nonlocal lock
                    if lock == False:
                        lock = True
                        if not hasattr(App.context, "network_test"):
                            try:
                                App.context.network_test = Network_test()
                            except Exception as e:
                                lock = False
                                raise Exception("Impossible to reach the server used for Network Test")


                        down_label.configure(text=str(0) + "Mbps")
                        up_label.configure(text=str(0) + "Mbps")
                        # progress bar create and starting
                        progress_bar_speedtest = customtkinter.CTkProgressBar(master=start_frame, mode="indeterminate")
                        progress_bar_speedtest.grid(row=1, column=0, sticky="nsew", pady=10)
                        progress_bar_speedtest.start()

                        def thread_factory(type):
                            nonlocal tmp_variable
                            if type == "download":
                                tmp_variable = App.context.network_test.test_download()
                            elif type == "upload":
                                tmp_variable = App.context.network_test.test_upload()

                        def thread_waiter_async(thread_to_wait, event, label, type):
                            thread_to_wait.join()
                            nonlocal tmp_variable
                            nonlocal lock
                            label.configure(text=str(tmp_variable) + "Mbps")
                            if type == "upload":
                                event.stop()
                                event.destroy()
                                lock = False

                        def thread_waiter_async_cascade(thread_event, thread_handler, thread_handler2):
                            thread_event.join()
                            thread_handler.start()
                            thread_handler2.start()

                        thread_download = threading.Thread(target=thread_factory, args=("download",))
                        thread_download.daemon = True
                        thread_download.start()
                        thread_waiter = threading.Thread(target=thread_waiter_async, args=(
                            thread_download, progress_bar_speedtest, down_label, "download"))
                        thread_waiter.daemon = True
                        thread_waiter.start()

                        thread_upload = threading.Thread(target=thread_factory, args=("upload",))
                        thread_upload.daemon = True
                        thread_waiter2 = threading.Thread(target=thread_waiter_async,
                                                          args=(thread_upload, progress_bar_speedtest, up_label, "upload"))
                        thread_waiter2.daemon = True

                        thread_waiter_cascade = threading.Thread(target=thread_waiter_async_cascade,
                                                                 args=(thread_waiter, thread_upload, thread_waiter2))
                        thread_waiter_cascade.daemon = True
                        thread_waiter_cascade.start()
                except Exception as e:
                    error_popup(e)

            # all labels with the default labels for download and other
            download_label = customtkinter.CTkLabel(master=speed_test_frame, text="Download:",
                                                    font=customtkinter.CTkFont(size=25, weight="bold"))
            download_label.grid(row=0, column=0, sticky="nw", padx=10)

            down_label = customtkinter.CTkLabel(master=speed_test_frame, text="0", font=customtkinter.CTkFont(size=20))
            down_label.grid(row=0, column=1, sticky="ne", padx=10)

            upload_label = customtkinter.CTkLabel(master=speed_test_frame, text="Upload:",
                                                  font=customtkinter.CTkFont(size=25, weight="bold"))
            upload_label.grid(row=1, column=0, sticky="nw", padx=10)

            up_label = customtkinter.CTkLabel(master=speed_test_frame, text="0", font=customtkinter.CTkFont(size=20))
            up_label.grid(row=1, column=1, sticky="ne", padx=10)

            # add an other frame to handle start button and progress bar
            start_frame = customtkinter.CTkFrame(master=speed_test_window, fg_color="transparent")
            start_frame.grid(row=1, padx=30, pady=30, sticky="n")

            # button to start speedtest
            start_button = customtkinter.CTkButton(master=start_frame, text="Start", command=start_speedtest)
            start_button.grid(row=2, column=0, sticky="n", pady=10)

            speedtest_icon = customtkinter.CTkLabel(master=start_frame, text="", image=self.speedtest_logo)
            speedtest_icon.grid(row=0, column=0, sticky="nsew")

            # progress bar
            # progress_bar_speedtest = customtkinter.CTkProgressBar(master=start_frame, mode="indeterminate")
            # progress_bar_speedtest.grid(row=0, column=0, sticky="nsew", pady=10)

        def welcome_page_comm():
            '''Welcome page is a simple dialog with all the main links and buttons to other dialogs, you can toggle if open or not at login with the checkbox'''
            # welcome frame and window
            welcome_window = customtkinter.CTkToplevel()
            welcome_window.geometry(f"600x650")
            welcome_window.title("Welcome to NetGun")

            frame_welcome = customtkinter.CTkFrame(master=welcome_window, fg_color="transparent")
            frame_welcome.grid(pady=30, padx=30, sticky="nsew")
            frame_welcome.place(relx=0.5, rely=0.5, anchor="c")

            image_label = customtkinter.CTkLabel(master=frame_welcome, text="", image=self.logo_icon, compound="top")
            image_label.grid(row=0, sticky="n", pady=15)
            # text box with label of welcome message
            welcome_label = customtkinter.CTkTextbox(master=frame_welcome, width=350, height=70, wrap="word")
            welcome_label.grid(row=1, sticky="w", pady=15)
            welcome_label.insert("end",
                                 "Benvenuto, questo è NetGun, il coltellino svizzero dei Penetration Tester, quì potrai trovare una suite di utilities da utilizzare durante il BlackBox Testing di Infrastrutture di rete.")
            welcome_label.configure(state="disabled")

            # button to open the manuale in a toplevel window
            manual_button = customtkinter.CTkButton(master=frame_welcome, text="Manual", image=self.document_logo,
                                                    compound="right", command=lambda: web.open("https://github.com/MyCr4ck/NetGun_Classe03/blob/main/Documentation/MANUALE%20D_USO.pdf", new=2),
                                                    font=customtkinter.CTkFont(size=18))
            manual_button.grid(row=2, sticky="nsew", pady=15)

            # button to open all links in the browser
            github_button = customtkinter.CTkButton(master=frame_welcome, text="Github", image=self.link_icon,
                                                    font=customtkinter.CTkFont(size=18), compound="right",
                                                    command=lambda: web.open(
                                                        "https://github.com/MyCr4ck/NetGun_Classe03", new=2))
            github_button.grid(row=3, sticky="nsew", pady=15)

            # button for speedtest internet connection
            speedtest_button = customtkinter.CTkButton(master=frame_welcome, text="SpeedTest Ookla",
                                                       image=self.shortcut_icon, compound="right",
                                                       font=customtkinter.CTkFont(size=18), command=speed_test_button)
            speedtest_button.grid(row=4, sticky="nsew", pady=15)

            # chech box if you want to open at startup
            chechbox_welcome = customtkinter.CTkCheckBox(master=frame_welcome, text="Apri al prossimo avvio",
                                                         variable=chechbox_welcome_var, onvalue="on", offvalue="off")
            chechbox_welcome.grid(row=5, sticky="sw", pady=50)

            def chechbox_save_button():
                chechbox_welcome_value = chechbox_welcome_var.get()

                config.read(conf_path)
                if config.has_section('welcome'):
                    config["welcome"]["open_login"] = str(chechbox_welcome_value)
                else:
                    config.add_section('welcome')
                    config["welcome"]["open_login"] = str(chechbox_welcome_value)

                with open(conf_path, 'w') as configfile:
                    config.write(configfile)

                welcome_window.destroy()

            # chech box save button
            chechbox_save = customtkinter.CTkButton(master=frame_welcome, text="Salva", image=self.save_icon,
                                                    font=customtkinter.CTkFont(size=18), compound="right",
                                                    command=chechbox_save_button)
            chechbox_save.grid(row=5, column=0, sticky="e", pady=10)

        def open_top_adv():
            '''Dialog checkbox for advanced options (OS detection, Disable PING, SYN scan, ACK scan), SYN and ACK are not compatible together, default it set all to none.'''
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
            opt4_var = customtkinter.StringVar()

            # all the options in examples for debugging purposes
            option1_check = customtkinter.CTkCheckBox(master=adv_frame, text="OS detection", variable=opt1_var,
                                                      onvalue="OS detection")
            option1_check.grid(row=0, column=0, sticky="n", pady=10)

            option2_check = customtkinter.CTkCheckBox(master=adv_frame, text="Disable PING", variable=opt2_var,
                                                      onvalue="Disable PING")
            option2_check.grid(row=1, column=0, sticky="n", pady=10)

            option3_check = customtkinter.CTkCheckBox(master=adv_frame, text="SYN scan", variable=opt3_var,
                                                      onvalue="SYN scan")
            option3_check.grid(row=2, column=0, sticky="n", pady=10)

            option4_check = customtkinter.CTkCheckBox(master=adv_frame, text="ACK scan", variable=opt4_var,
                                                      onvalue="ACK scan")
            option4_check.grid(row=3, column=0, sticky="n", pady=10)

            if App.context.option_var1 != '':
                option1_check.select()
            if App.context.option_var2 != '':
                option2_check.select()
            if App.context.option_var3 != '':
                option3_check.select()
            if App.context.option_var4 != '':
                option4_check.select()

            # button to kill the window and store the variables
            kill_button = customtkinter.CTkButton(master=adv_frame, text="OK", command=lambda: kill_window(adv_window))
            kill_button.grid(row=4, sticky="se", padx=30, pady=30)

            def kill_window(top):
                # storing variables and printing for debugging
                App.context.option_var1 = opt1_var.get()
                if App.context.option_var1 == "0":
                    App.context.option_var1 = ""

                App.context.option_var2 = opt2_var.get()
                if App.context.option_var2 == "0":
                    App.context.option_var2 = ""

                App.context.option_var3 = opt3_var.get()
                if App.context.option_var3 == "0":
                    App.context.option_var3 = ""

                App.context.option_var4 = opt4_var.get()
                if App.context.option_var4 == "0":
                    App.context.option_var4 = ""

                print("Advanced: {} {} {} {}".format(App.context.option_var1, App.context.option_var2,
                                                     App.context.option_var3, App.context.option_var4))
                top.destroy()

        # a debugging function in terminal
        def start_scan():
            '''The scan itself is powered bu nmap, it takes ip, port, advanced options, aggressivity and mode from other fields and start scanning'''
            try:
                def scan_observer(progress_bar, scan_object, result, values):

                    thread = threading.Thread(target=start_scan_process, args=(scan_object, result))
                    thread.daemon = True
                    thread.start()

                    thread.join()
                    progress_bar.stop()
                    scan_end(values)

                def start_scan_process(scan_object, result):
                    result.update(scan_object.start_scan())

                print("Starting scan...")
                if hasattr(self, "tree_frame"):
                    self.tree_frame = customtkinter.CTkFrame(self.main_frame, height=400, width=1200)
                    self.tree_frame.grid(row=2, column=0, sticky="nsew", padx=40, pady=20)
                if hasattr(self, "scan_tree"):
                    self.scan_tree.grid_forget()
                if hasattr(self, "tips_button"):
                    self.tips_button.grid_forget()
                if hasattr(self, "cve_button"):
                    self.cve_button.grid_forget()
                if hasattr(self, "misconf_button"):
                    self.misconf_button.grid_forget()
                if hasattr(self, "status_label"):
                    self.status_label.grid_forget()
                if hasattr(self, "scan_os"):
                    self.scan_os.grid_forget()
                if hasattr(self, "scan_tree_scroll"):
                    self.scan_tree_scroll.grid_forget()

                ip = ip_var.get()
                port = port_var.get()
                tcp_udp = tcp_udp_var.get()
                scan_type = scan_type_var.get()
                scan_aggro = int(scan_aggro_var.get())
                App.context.advanced_option_list = [x for x in list(
                    (App.context.option_var1, App.context.option_var2, App.context.option_var3, App.context.option_var4)) if
                                                    x != ""]

                print("Ip: {}".format(ip))
                print("Port: {}".format(port))
                print("TCP/UDP: {}".format(tcp_udp))
                print("Type: {}".format(scan_type))
                print("Aggro: {}".format(scan_aggro))
                print("Advanced: {} {} {} {}".format(App.context.option_var1, App.context.option_var2,
                                                     App.context.option_var3, App.context.option_var4))
                print("Advanced_Option_List: ", App.context.advanced_option_list)

                style = ttk.Style()
                style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                                font=('Calibri', 12))  # Modify the font of the body

                style.configure("mystyle.Treeview.Heading", font=('Calibri', 15, 'bold'))  # Modify the font of the headings
                style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders
                # initialize tree structure
                self.scan_tree = ttk.Treeview(self.tree_frame, height=15, style="mystyle.Treeview")

                # progress bar
                self.scan_progress = customtkinter.CTkProgressBar(master=self.main_frame, mode="indeterminate")
                # the progress bar needs the label too
                self.scan_verbose = customtkinter.CTkLabel(master=self.main_frame, text="Scanning...",
                                                           font=customtkinter.CTkFont(size=25, weight="bold"))
                # label scannning
                self.scan_verbose.grid(row=3, column=0, sticky="nsew", pady=10, padx=30)
                # let appear the progress bar and start
                self.scan_progress.grid(row=4, column=0, sticky="nsew", pady=10, padx=30)

                # set number columns
                self.scan_tree["columns"] = ("colonna1", "colonna2", "colonna3")

                self.scan_tree.heading("#0", text="PORT")
                self.scan_tree.heading("colonna1", text="State")
                self.scan_tree.heading("colonna2", text="Service")
                self.scan_tree.heading("colonna3", text="Version")
                self.scan_tree.column("colonna1", stretch=NO, width=265)
                self.scan_tree.column("colonna2", stretch=NO, width=265)
                self.scan_tree.column("colonna3", stretch=NO, width=450)


                # date examples
                App.context.target = Target(ip, port)
                App.context.filter = Filter(tcp_udp.lower(), App.context.advanced_option_list, scan_aggro)

                scan_tmp = Scan(App.context.target, App.context.filter, scan_type)

                result = {}

                shared_values = (result, self.scan_tree, scan_type)
                thread_scan_observer = threading.Thread(target=scan_observer,
                                                        args=(self.scan_progress, scan_tmp, result, shared_values))
                thread_scan_observer.daemon = True

                thread_scan_observer.start()
                self.scan_progress.start()
            except Exception as e:
                error_popup(e)

        def scan_end(values):
            result, scan_tree, scan_type = values
            App.context.scan_result = scan_result.Scan_result(result)
            App.context.scan_result.cve_tmp = {}
            pprint(result)

            for name, values in App.context.scan_result.result["ports"].items():
                if scan_type == "DEEP":
                    # add single element to the treeview
                    scan_tree.insert("", "end", text=name, values=(values['state'], values['service'], values['version']))
                else:
                    scan_tree.insert("", "end", text=name, values=(values['state'], values['service'], ''))

            self.scan_progress.grid_forget()
            self.scan_verbose.grid_forget()

            print("Scan finished.")

            # positioning the treeview when start scanning
            scan_tree.grid(row=2, column=0, sticky="nsew")

            self.status_name = "Status: " + App.context.scan_result.result["status"]
            self.status_label = customtkinter.CTkLabel(master=self.tree_frame, text=self.status_name, font=customtkinter.CTkFont(size=20, weight="bold"))
            self.status_label.grid(row=0, column=0, pady=10, sticky="nw")

            if "os" in App.context.scan_result.result:
                if "name" in App.context.scan_result.result["os"]:
                    self.os_name = "OS: " + App.context.scan_result.result["os"]["name"]
            else:
                self.os_name = "OS: Not Found"

            self.scan_os = customtkinter.CTkLabel(master=self.tree_frame, text=self.os_name, font=customtkinter.CTkFont(size=20, weight="bold"))
            self.scan_os.grid(row=1, column=0, pady=10, sticky="nw")

            # add the scrollbar
            self.scan_tree_scroll = customtkinter.CTkScrollbar(self.tree_frame, command=scan_tree.yview)
            self.scan_tree_scroll.grid(row=2, column=1, sticky="nsw")
            self.scan_tree.configure(yscrollcommand=self.scan_tree_scroll.set)

            def cve_button_click():
                '''Open a dialog with the common CVE and Vulnerabilty, all link can be selected and opened'''
                try:
                    # takes the element in the table
                    item_focus = scan_tree.focus()

                    # takes name and version
                    name_focus = scan_tree.item(item_focus, "text")
                    if name_focus == "":
                        raise Exception("Nessun servizio selezionato!")

                    version_focus = App.context.scan_result.result['ports'][name_focus]['version']

                    # find all the cve here and codes after start the tree
                    global data_cve

                    data_cve = Cve(version_focus).search_cve()

                    # create a top level window
                    top_cve = customtkinter.CTkToplevel()
                    top_cve.geometry(f"900x700")
                    top_cve.title(name_focus)

                    main_frame_cve = customtkinter.CTkFrame(top_cve, fg_color="transparent")
                    main_frame_cve.grid(sticky="nsew")
                    main_frame_cve.place(relx=0.5, rely=0.5, anchor="c")

                    # adding all the frame i need (3)
                    frame_cve_1 = customtkinter.CTkFrame(main_frame_cve, width=800)
                    frame_cve_1.grid(row=0, column=0, pady=10, padx=10, sticky="new")

                    # adding a frame only to separate frames
                    sep = customtkinter.CTkFrame(frame_cve_1, fg_color="transparent", height=50)
                    sep.grid(row=0, column=1, padx=10)

                    frame_cve_2 = customtkinter.CTkFrame(main_frame_cve, height=300)
                    frame_cve_2.grid(row=1, column=0, pady=10, padx=10, sticky="nsew")

                    frame_cve_3 = customtkinter.CTkFrame(main_frame_cve, height=50, fg_color="transparent")
                    frame_cve_3.grid(row=2, column=0, pady=10, padx=10, sticky="sew")

                    servicing = "Service:   {}".format(version_focus)
                    # services label in the right
                    label_services = customtkinter.CTkLabel(frame_cve_1, text=servicing,
                                                            font=customtkinter.CTkFont(size=15, weight="bold"),
                                                            text_color="white")
                    label_services.grid(row=0, column=2)

                    # progress bar for research cve
                    prog_bar = customtkinter.CTkProgressBar(frame_cve_3, mode="indeterminate")
                    prog_bar.grid(row=2, column=0, pady=10)
                    prog_bar.start()

                    tree_cve = ttk.Treeview(frame_cve_2, height=10)

                    tree_cve["columns"] = ("colonna1", "colonna2")

                    tree_cve.heading("#0", text="ID")
                    tree_cve.heading("colonna1", text="Description")
                    tree_cve.heading("colonna2", text="Reference")

                    App.context.number_cve = 0

                    # for name, values in data_cve.items():
                    for i in range(len(data_cve)):
                        tree_cve.insert("", "end", text=data_cve[i]['id'],
                                        values=(data_cve[i]['description'], data_cve[i]['resource']))
                        App.context.number_cve += 1

                    App.context.scan_result.cve_tmp[version_focus] = data_cve

                    tree_cve.column("#0", width=150)
                    tree_cve.column("colonna1", width=500)
                    tree_cve.column("colonna2", width=150)

                    # debugging varaible for the numbers of cve on a single service
                    # add 2 text boxes on the top left and right
                    text_cve = customtkinter.CTkLabel(master=frame_cve_1, height=70,
                                                      font=customtkinter.CTkFont(size=15, weight="bold"),
                                                      text_color="white")
                    # need for the color change
                    if App.context.number_cve <= 5:
                        text_cve.configure(fg_color="green")
                    elif 6 <= App.context.number_cve <= 15:
                        text_cve.configure(fg_color="orange")
                    else:
                        text_cve.configure(fg_color="red")

                    # stopping prog bar
                    prog_bar.stop()
                    prog_bar.destroy()

                    texting = "Numbers of CVE:  {}".format(App.context.number_cve)
                    text_cve.configure(text=texting, corner_radius=6)
                    text_cve.grid(row=0, column=0, sticky="w")

                    tree_cve.grid(row=0, column=0, sticky="nsew")  # positioning the tree
                    # set the scrollbar
                    tree_cve_scroll = customtkinter.CTkScrollbar(frame_cve_2, command=scan_tree.yview)
                    tree_cve_scroll.grid(row=0, column=1, sticky="nsw")
                    tree_cve.configure(yscrollcommand=self.scan_tree_scroll.set)

                    def open_link():
                        item_link = tree_cve.focus()

                        name_link = tree_cve.item(item_link, "text")
                        link = ""
                        for number in range(len(data_cve)):
                            if name_link in data_cve[number].values():
                                link = data_cve[number]['resource']

                        if link == "":
                            error_popup(Exception("Link not found!"))
                        web.open(link, new=2)

                    link_button = customtkinter.CTkButton(master=frame_cve_2, text="Open Link", image=self.link_icon,
                                                          compound="right", command=open_link,
                                                          font=customtkinter.CTkFont(size=20, weight="bold"))
                    link_button.grid(row=1, column=0, sticky="sew", pady=10)
                except Exception as request_exception:
                    error_popup(request_exception)

            def tips_button_click():
                '''This dialog would show simple tips'''
                try:
                    item_focus = scan_tree.focus()

                    # takes name and service
                    name_focus = scan_tree.item(item_focus, "text")
                    if name_focus == "":
                        raise Exception("Nessun servizio selezionato!!")
                    service_focus = App.context.scan_result.result["ports"][name_focus]['service']

                    # create a top level window
                    top_tips = customtkinter.CTkToplevel()
                    top_tips.geometry(f"700x500")
                    top_tips.title("Tips")

                    tips_frame_main = customtkinter.CTkFrame(top_tips)
                    tips_frame_main.grid(sticky="nsew")
                    tips_frame_main.place(relx=0.5, rely=0.5, anchor="c")

                    # acronym of the service
                    tip = App.context.tip[service_focus]
                    name = tip.name
                    default_port = tip.default_port
                    description = tip.description

                    acronym_frame = customtkinter.CTkFrame(tips_frame_main)
                    acronym_frame.grid(sticky="nsew")

                    acronym_label = customtkinter.CTkLabel(master=acronym_frame, text="Service: ",
                                                           font=customtkinter.CTkFont(size=18,weight="bold"),
                                                           text_color="white", fg_color="blue")
                    acronym_label.grid(row=0, column=0, sticky="nw", padx=10)

                    acronym_label2 =customtkinter.CTkLabel(master=acronym_frame, text=name,
                                                           font=customtkinter.CTkFont(size=18))
                    acronym_label2.grid(row=0, column=1, sticky="nw", padx=10)

                    def_port = customtkinter.CTkLabel(master=acronym_frame, text="Default Port: ",
                                                      font=customtkinter.CTkFont(size=18,weight="bold"),
                                                           text_color="white", fg_color="blue")
                    def_port.grid(row=0, column=2, sticky="ne", padx=10)

                    def_port2 = customtkinter.CTkLabel(master=acronym_frame, text=default_port,
                                                      font=customtkinter.CTkFont(size=18))
                    def_port2.grid(row=0, column=3, sticky="ne", padx=10)

                    #description_serv = customtkinter.CTkLabel(master=tips_frame_main, text=description)
                    #description_serv.grid(row=1, column=0, sticky="nsew")
                    description_serv = customtkinter.CTkTextbox(
                        master=tips_frame_main, wrap="word", width=500, font=main_font)
                    description_serv.grid(
                        row=1, column=0, sticky="nsew", pady=20)
                    description_serv.insert("end", description)
                    description_serv.configure(state="disabled")
                except Exception as e:
                    error_popup(e)

            def misconf_button_click():
                '''Misconfiguration for the selected service, most common ones will open'''
                try:
                    item_focus = scan_tree.focus()

                    # takes name and service
                    name_focus = scan_tree.item(item_focus, "text")
                    if name_focus == "":
                        raise Exception("Nessun servizio selezionato!!")

                    service_focus = App.context.scan_result.result["ports"][name_focus]['service']
                    # if service_focus not in App.context.misconfiguration:
                    #    raise Exception("Misconfiguration data not available for service: " + service_focus)

                    # name_focus = "Names focus" #scan_tree.item(item_focus, "text")
                    # service_focus = "Service focus name" #App.context.scan_result.result[name]['service']

                    # data
                    path = "../persistence/storage/misconfiguration.xml"
                    service_misconf = App.context.misconfiguration
                    misconf = service_misconf.misconfigurations_dict[service_focus]

                    # create a top level window
                    top_misconf = customtkinter.CTkToplevel()
                    top_misconf.geometry(f"750x700")
                    top_misconf.title("Misconfiguration")

                    misconf_frame = customtkinter.CTkScrollableFrame(top_misconf, fg_color="transparent", width=700, height=650)
                    misconf_frame.grid(sticky="nsew")
                    misconf_frame.place(relx=0.5, rely=0.5, anchor="c")

                    service_label = customtkinter.CTkLabel(misconf_frame, text=service_focus,
                                                           font=customtkinter.CTkFont(size=35, weight="bold"))
                    service_label.grid(row=0, sticky="new", pady=10, padx=30)

                    # carlo sei bello come gravino
                    f = 1
                    for i in misconf:
                        misconf_tool_installation = i.tool_installation
                        misconf_test_type = i.testType
                        misconf_description = i.description
                        misconf_command = i.command

                        test_type = customtkinter.CTkLabel(misconf_frame, text=misconf_test_type,
                                                           font=customtkinter.CTkFont(size=18, weight="bold"),
                                                           fg_color="#008bd3", text_color="white",
                                                           corner_radius=5)
                        test_type.grid(row=f, column=0, sticky="nsew", pady=10)
                        f += 1
                        description_label = customtkinter.CTkTextbox(misconf_frame, wrap="word", font=main_font)
                        description_label.grid(row=f, column=0, sticky="nsew", pady=10)
                        new_miscon = "Description:\n" + misconf_description
                        description_label.insert("end", new_miscon)
                        description_label.configure(state="disabled", fg_color="transparent")


                        f += 1
                        tool_install = customtkinter.CTkTextbox(master=misconf_frame, wrap="word", height=80, width=650,
                                                                font=main_font)
                        tool_install.grid(row=f, column=0, sticky="nsew", pady=10)
                        tool_install.insert("end", misconf_tool_installation)
                        tool_install.configure(state="disabled")

                        f += 1

                        command_tool = customtkinter.CTkButton(master=misconf_frame, text="Install",width=main_width, height=main_height,
                                                                 image=self.shortcut_icon,
                                                                 compound="right", command=i.install_tool,
                                                                 font=main_font)
                        command_tool.grid(row=f, column=0, sticky="se", pady=10)

                        f += 1

                        command_textbox = customtkinter.CTkTextbox(master=misconf_frame, wrap="word", height=80,width=650,
                                                                   font=main_font)
                        command_textbox.grid(row=f, column=0, sticky="nsew", pady=10)
                        command_textbox.insert("end", misconf_command)
                        command_textbox.configure(state="disabled")

                        f += 1

                        command_esegui = customtkinter.CTkButton(master=misconf_frame, text="RUN", image=self.shortcut_icon,
                                                  compound="right", command=i.test_misconfiguration,width=main_width, height=main_height,
                                                  font=main_font)
                        command_esegui.grid(row=f, column=0, sticky="se", pady=10)

                        f += 1
                except Exception as e:
                    error_popup(e)

            # frame for more buttons
            more_frame = customtkinter.CTkFrame(self.tree_frame, width=500, fg_color="transparent")
            more_frame.grid(row=3, column=0, sticky="nsew")

            # more buttons
            tips_button = customtkinter.CTkButton(master=more_frame, text="Tips", image=self.shortcut_icon,
                                                  compound="right", command=tips_button_click,
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
            self.tips_button = tips_button
            tips_button.grid(row=0, column=0, sticky="nsew", pady=10, padx=30)

            misconf_button = customtkinter.CTkButton(master=more_frame, text="Misconfiguration",
                                                     image=self.shortcut_icon, compound="right",
                                                     command=misconf_button_click,
                                                     font=customtkinter.CTkFont(size=20, weight="bold"))
            self.misconf_button = misconf_button
            misconf_button.grid(row=0, column=1, sticky="nsew", pady=10, padx=30)

            # button to open the cve file
            cve_button = customtkinter.CTkButton(master=more_frame, text="Open CVE", image=self.shortcut_icon,
                                                 compound="right", command=cve_button_click,
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
            self.cve_button = cve_button

            cve_button.grid(row=0, column=2, sticky="nsew", pady=10, padx=30)

            if scan_type == "SHALLOW":
                cve_button.destroy()


        def export_file():
            '''Export file will open a dialog window to select the path to save the file report.pdf'''

            try:
                file = filedialog.asksaveasfilename(filetypes=[("PDF file", "*.pdf")],
                                                    defaultextension='.pdf',
                                                    title='Export Report')
                # fob = open(file, 'w')
                # fob.write("Hello, world!")
                # fob.close()
                if hasattr(App.context, 'scan_result'):
                    App.context.scan_result.result['Vulnerabilities'] = {'service': App.context.scan_result.cve_tmp}
                    pprint(App.context.scan_result.result)
                    report = Report(file)
                    report.create_report(App.context.scan_result.result)
            except Exception as e:
                error_popup(e)
 
        # main frame with options and label
        self.main_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(sticky="nsew")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="c")

        # label title of NetGun
        self.main_frame_label = customtkinter.CTkLabel(self.main_frame, text=" NetGun", image=self.logo_icon,
                                                       compound="left",
                                                       font=customtkinter.CTkFont(size=40, weight="bold"))
        self.main_frame_label.grid(row=0, column=0, sticky="nw")

        # options button
        self.options_button = customtkinter.CTkButton(self.main_frame, text="", image=self.option_icon, compound="top",
                                                      command=options_settings, width=quadr_width, height=quadr_height)
        self.options_button.grid(row=0, column=1, sticky="e")

        # buttons and text in main
        # set the frame first in the center of main_frame
        self.center_frame = customtkinter.CTkFrame(self.main_frame, fg_color="transparent")
        self.center_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=20)

        # placeholders entry
        '''Ip placeholder, here will go the ip address. EXAMPLE: "192.168.1.109"'''
        self.ip_entry = customtkinter.CTkEntry(master=self.center_frame, placeholder_text="IP Address",
                                               textvariable=ip_var, width=main_width, height=main_height,
                                               font=main_font)
        self.ip_entry.grid(row=0, column=0, sticky="w", padx=10)

        '''Port placeholder, here will go the port range. EXAMPLE: "1-104"'''
        self.port_entry = customtkinter.CTkEntry(master=self.center_frame, placeholder_text="Port",
                                                 textvariable=port_var, width=main_width, height=main_height, font=main_font)
        self.port_entry.grid(row=0, column=1, sticky="w", padx=10)

        # option menus
        '''TCP/UDP, select one of the 2 types. EXAMPLE: "TCP"'''
        self.tcp_udp_option = customtkinter.CTkOptionMenu(master=self.center_frame, values=["TCP", "UDP"],
                                                          variable=tcp_udp_var, width=main_width, height=main_height, font=main_font)
        self.tcp_udp_option.grid(row=0, column=2, sticky="w", padx=10)

        # advanced settings to top level with all check box
        self.type_adv_option = customtkinter.CTkButton(master=self.center_frame, text="Advanced",
                                                       image=self.shortcut_icon, compound="right", command=open_top_adv,
                                                       width=main_width, height=main_height, font=main_font)
        self.type_adv_option.grid(row=0, column=3, sticky="w", padx=10)

        # other options menu
        '''The scan type mode, how hard can be the scan, select one of the list, default is SHALLOW. EXAMPLE: "DEEP"'''
        self.scan_type_option = customtkinter.CTkOptionMenu(master=self.center_frame, values=["SHALLOW", "DEEP"],
                                                            variable=scan_type_var, width=main_width, height=main_height, font=main_font)
        self.scan_type_option.grid(row=0, column=4, sticky="w", padx=10)

        '''Aggressivity placeholder, aggressivity misured in a scale 0 to 4, from the slowest to the fastest. EXAMPLE: "4"'''
        self.scan_aggro_option = customtkinter.CTkOptionMenu(master=self.center_frame, values=["0", "1", "2", "3", "4"],
                                                             variable=scan_aggro_var, width=quadr_width, height=quadr_height, font=main_font)
        self.scan_aggro_option.grid(row=0, column=5, sticky="w", padx=10)

        # button scan
        self.scan_button = customtkinter.CTkButton(self.center_frame, text="Scan ", image=self.search_logo,
                                                   compound="right", font=main_font, width=main_width,
                                                   height=main_height, command=start_scan)
        self.scan_button.grid(row=0, column=6, sticky="nsew", padx=10)

        # frame with a tree view for the table
        #self.tree_frame = customtkinter.CTkFrame(self.main_frame, height=300)
        #self.tree_frame.grid(row=2, column=0, sticky="nsew", padx=40, pady=20)
        self.tree_frame = customtkinter.CTkFrame(self.main_frame, height=400, width=1200)
        self.tree_frame.grid(row=2, column=0, sticky="nsew", padx=40, pady=20)

        # report folder button
        self.report_button_folder = customtkinter.CTkButton(self.main_frame, text="Export Report  ",
                                                            image=self.folder_icon, compound="right", anchor="e",
                                                            command=export_file, width=main_width, height=main_height, font=main_font)
        self.report_button_folder.grid(row=5, column=0, padx=10, pady=50, sticky="se")

        # welcome frame button on the bottom main frame
        self.welcome_button = customtkinter.CTkButton(self.main_frame, text="", image=self.profile_icon,
                                                      command=welcome_page_comm, width=quadr_width, height=quadr_height)
        self.welcome_button.grid(row=5, column=1, sticky="se", pady=50)

        # start the welcome message at login
        if welcom_conf == "on":
            welcome_page_comm()

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


    app = App()
    app.mainloop()
