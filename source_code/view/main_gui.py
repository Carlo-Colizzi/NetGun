import multiprocessing
import sys
from pprint import pprint

sys.path.insert(0, "../../../NetGun_Classe03")
from source_code.business_logic.cve_exploit.cve import Cve
from source_code.business_logic.scanner.filter import Filter
from source_code.business_logic.scanner.scan import Scan
from source_code.business_logic.scanner.target import Target
from source_code.business_logic.report_py.report import Report
import threading
import asyncio
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import customtkinter
import screeninfo
import webbrowser as web
import os
import configparser
from PIL import Image
from source_code.business_logic.test_network_performance.network_test import Network_test
from source_code.business_logic.application_context.context import Context
from source_code.business_logic.scanner import scan, scan_result

print(vars())


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

        self.error_icon = customtkinter.CTkImage(Image.open(os.path.join(icon_path, "error_icon.png")), size=(20, 20))

        # configuration window main
        self.title("NetGun")
        self.geometry(f"1920x1080")  # default geometry
        # self.geometry("{}x{}".format(mon_width, mon_height))
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

        color_option_variable = customtkinter.StringVar(value=system_color)
        ip_var = customtkinter.StringVar(value="127.0.0.1")
        port_var = customtkinter.StringVar(value="1-1024")
        tcp_udp_var = customtkinter.StringVar(value="TCP")
        scan_type_var = customtkinter.StringVar(value="DEEP")
        scan_aggro_var = customtkinter.StringVar(value="2")
        chechbox_welcome_var = customtkinter.StringVar(value=welcom_conf)

        def error_popup(exception):
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
                        progress_bar_speedtest.grid(row=0, column=0, sticky="nsew", pady=10)
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

            speedtest_icon = customtkinter.CTkLabel(master=speed_test_frame, text="", image=self.speedtest_logo)
            speedtest_icon.grid(row=2, column=0, sticky="nse")

            # add an other frame to handle start button and progress bar
            start_frame = customtkinter.CTkFrame(master=speed_test_window)
            start_frame.grid(row=1, padx=30, pady=30, sticky="n")

            # button to start speedtest
            start_button = customtkinter.CTkButton(master=start_frame, text="Start", command=start_speedtest)
            start_button.grid(row=1, column=0, sticky="n", pady=10)

            # progress bar
            # progress_bar_speedtest = customtkinter.CTkProgressBar(master=start_frame, mode="indeterminate")
            # progress_bar_speedtest.grid(row=0, column=0, sticky="nsew", pady=10)

        def welcome_page_comm():
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
                                 "Benvenuto, questo è NetGun, il programma perfetto per esperti e non, in ambito di ethical hacking. Buon hack a tutti!")
            welcome_label.configure(state="disabled")

            # button to open the manuale in a toplevel window
            manual_button = customtkinter.CTkButton(master=frame_welcome, text="Manual", image=self.document_logo,
                                                    compound="right", command=manual_command,
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
            try:
                def scan_observer(progress_bar, scan_object, result,values):

                    thread = threading.Thread(target=start_scan_process, args=(scan_object, result))
                    thread.daemon = True
                    thread.start()

                    thread.join()
                    progress_bar.stop()
                    scan_end(values)

                def start_scan_process(scan_object, result):
                    result.update(scan_object.start_scan())

                print("Starting scan...")

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
                print("Advanced: {} {} {} {}".format(App.context.option_var1, App.context.option_var2, App.context.option_var3, App.context.option_var4))
                print("Advanced_Option_List: ", App.context.advanced_option_list)

                # initialize tree structure
                scan_tree = ttk.Treeview(self.tree_frame, height=10)

                # progress bar, implemented but not started yet
                self.scan_progress = customtkinter.CTkProgressBar(master=self.main_frame, mode="indeterminate")
                # the progress bar needs the label too
                self.scan_verbose = customtkinter.CTkLabel(master=self.main_frame, text="Scanning...")
                # label scannning
                self.scan_verbose.grid(row=3, column=1, sticky="nw", pady=10)

                # let appear the progress bar and start
                self.scan_progress.grid(row=3, column=0, sticky="nw", pady=10)

                # set number columns
                scan_tree["columns"] = ("colonna1", "colonna2", "colonna3")

                scan_tree.heading("#0", text="PORT")
                scan_tree.heading("colonna1", text="Service")
                scan_tree.heading("colonna2", text="Version")
                scan_tree.heading("colonna3", text="State")

                # date examples
                App.context.target = Target(ip, port)
                App.context.filter = Filter(tcp_udp.lower(), App.context.advanced_option_list, scan_aggro)

                scan_tmp = Scan(App.context.target, App.context.filter, scan_type)

                result = {}

                shared_values = (result, scan_tree, scan_type)
                thread_scan_observer = threading.Thread(target=scan_observer, args=(self.scan_progress, scan_tmp, result, shared_values))
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

            self.scan_progress.destroy()
            self.scan_verbose.destroy()

            print("Scan finished.")

            # positioning the treeview when start scanning
            scan_tree.grid(row=0, column=0, sticky="nsew")
            # add the scrollbar
            scan_tree_scroll = customtkinter.CTkScrollbar(self.tree_frame, command=scan_tree.yview)
            scan_tree_scroll.grid(row=0, column=1, sticky="nsw")
            scan_tree.configure(yscrollcommand=scan_tree_scroll.set)



            def cve_button_click():
                # takes the element in the table
                item_focus = scan_tree.focus()

                # takes name and version
                name_focus = scan_tree.item(item_focus, "text")
                version_focus = App.context.scan_result.result['ports'][name_focus]['version']

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

                # find all the cve here and codes after start the tree
                global data_cve
                data_cve = Cve(version_focus).search_cve()

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
                tree_cve.configure(yscrollcommand=scan_tree_scroll.set)

                def open_link():
                    item_link = tree_cve.focus()

                    name_link = tree_cve.item(item_link, "text")
                    url_link = data_cve[name_link][0]['resource']

                    web.open(url_link, new=2)

                link_button = customtkinter.CTkButton(master=frame_cve_2, text="Open Link", image=self.link_icon,
                                                      compound="right", command=open_link,
                                                      font=customtkinter.CTkFont(size=20, weight="bold"))
                link_button.grid(row=1, column=0, sticky="sew", pady=10)

            def tips_button_click():
                item_focus = scan_tree.focus()

                # takes name and service
                name_focus = scan_tree.item(item_focus, "text")
                service_focus = App.context.scan_result.result[name]['service']

                # create a top level window
                top_tips = customtkinter.CTkToplevel()
                top_tips.geometry(f"900x700")
                top_tips.title("Tips")

                tips_frame_main = customtkinter.CTkFrame(top_tips)
                tips_frame_main.grid(sticky="nsew")
                tips_frame_main.place(relx=0.5, rely=0.5, anchor="c")

                # acronym of the service
                acronym_text = "Acronym:" + service_focus

                acronym_label = customtkinter.CTkLabel(master=tips_frame_main, text=acronym_text,
                                                       font=customtkinter.CTkFont(size=18))
                acronym_label.grid(row=0, column=0, sticky="nw")

                def_port = customtkinter.CTkLabel(master=tips_frame_main, text=name_focus,
                                                  font=customtkinter.CTkFont(size=18))
                def_port.grid(row=0, column=1, sticky="ne")

                description_serv = customtkinter.CTkLabel(master=tips_frame_main, text="Description should be there")
                description_serv.grid(row=1, column=0, sticky="nsew")

            def misconf_button_click():
                item_focus = scan_tree.focus()

                # takes name and service
                name_focus = scan_tree.item(item_focus, "text")
                service_focus = App.context.scan_result.result[name]['service']

                # create a top level window
                top_misconf = customtkinter.CTkToplevel()
                top_misconf.geometry(f"900x700")
                top_misconf.title("Misconfiguration")

            def delete_wid_frame():
                for widget in self.tree_frame.winfo_children():
                    widget.destroy()

                for widget in more_frame.winfo_children():
                    widget.destroy()

            # frame for more buttons
            more_frame = customtkinter.CTkFrame(self.tree_frame, width=500, fg_color="transparent")
            more_frame.grid(row=1, column=0, sticky="nsew")

            # more buttons
            tips_button = customtkinter.CTkButton(master=more_frame, text="Tips", image=self.shortcut_icon,
                                                  compound="right", command=tips_button_click,
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
            tips_button.grid(row=0, column=0, sticky="nsew", pady=10, padx=20)

            misconf_button = customtkinter.CTkButton(master=more_frame, text="Misconfiguration",
                                                     image=self.shortcut_icon, compound="right",
                                                     command=misconf_button_click,
                                                     font=customtkinter.CTkFont(size=20, weight="bold"))
            misconf_button.grid(row=0, column=1, sticky="nsew", pady=10, padx=20)

            # button to open the cve file
            cve_button = customtkinter.CTkButton(master=more_frame, text="Open CVE", image=self.shortcut_icon,
                                                 compound="right", command=cve_button_click,
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))

            cve_button.grid(row=0, column=2, sticky="nsew", pady=10, padx=20)

            if scan_type == "SHALLOW":
                cve_button.destroy()


            cancel_button = customtkinter.CTkButton(master=more_frame, text="Clear", command=delete_wid_frame,
                                                    font=customtkinter.CTkFont(size=20, weight="bold"))
            cancel_button.grid(row=0, column=3, sticky="nsew", pady=10, padx=20)

        def export_file():
            file = filedialog.asksaveasfilename(filetypes=[("PDF file", "*.pdf")],
                                                defaultextension='.pdf',
                                                title='Export Report')
            # fob = open(file, 'w')
            # fob.write("Hello, world!")
            # fob.close()
            if hasattr(App.context, 'scan_result'):
                App.context.scan_result.result['Vulnerabilities'] = {'service': App.context.scan_result.cve_tmp}
                report = Report(file)
                report.create_report(App.context.scan_result.result)
        
        # main frame with options and label
        self.main_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(sticky="nsew")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="c")

        # label
        self.main_frame_label = customtkinter.CTkLabel(self.main_frame, text=" NetGun", image=self.logo_icon,
                                                       compound="left",
                                                       font=customtkinter.CTkFont(size=40, weight="bold"))
        self.main_frame_label.grid(row=0, column=0, sticky="nw")

        # options button
        self.options_button = customtkinter.CTkButton(self.main_frame, text="", image=self.option_icon, compound="top",
                                                      command=options_settings, width=25)
        self.options_button.grid(row=0, column=1, sticky="e")

        # buttons and text in main
        # set the frame first in the center of main_frame
        self.center_frame = customtkinter.CTkFrame(self.main_frame, fg_color="transparent")
        self.center_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=20)

        '''Step through every column from the first column to the last column'''
        # placeholders entry
        self.ip_entry = customtkinter.CTkEntry(master=self.center_frame, placeholder_text="IP Address",
                                               textvariable=ip_var)
        self.ip_entry.grid(row=0, column=0, sticky="w", padx=10)

        self.port_entry = customtkinter.CTkEntry(master=self.center_frame, placeholder_text="Port",
                                                 textvariable=port_var, width=90)
        self.port_entry.grid(row=0, column=1, sticky="w", padx=10)

        # option menus
        self.tcp_udp_option = customtkinter.CTkOptionMenu(master=self.center_frame, values=["TCP", "UDP"],
                                                          variable=tcp_udp_var, width=100)
        self.tcp_udp_option.grid(row=0, column=2, sticky="w", padx=10)

        # advanced settings to top level with all check box
        self.type_adv_option = customtkinter.CTkButton(master=self.center_frame, text="Advanced",
                                                       image=self.shortcut_icon, compound="right", command=open_top_adv,
                                                       width=100)
        self.type_adv_option.grid(row=0, column=3, sticky="w", padx=10)

        # other options menu
        self.scan_type_option = customtkinter.CTkOptionMenu(master=self.center_frame, values=["SHALLOW", "DEEP"],
                                                            variable=scan_type_var, width=100)
        self.scan_type_option.grid(row=0, column=4, sticky="w", padx=10)

        self.scan_aggro_option = customtkinter.CTkOptionMenu(master=self.center_frame, values=["0", "1", "2", "3", "4"],
                                                             variable=scan_aggro_var, width=10)
        self.scan_aggro_option.grid(row=0, column=5, sticky="w", padx=10)

        # button scan
        self.scan_button = customtkinter.CTkButton(self.center_frame, text="Scan ", image=self.search_logo,
                                                   compound="right", font=customtkinter.CTkFont(size=18), width=70,
                                                   height=25, command=start_scan)
        self.scan_button.grid(row=0, column=6, sticky="nsew", padx=10)

        # frame with a tree view for the table
        self.tree_frame = customtkinter.CTkFrame(self.main_frame, height=300)
        self.tree_frame.grid(row=2, column=0, sticky="nsew", padx=40, pady=20)

        # report folder button
        self.report_button_folder = customtkinter.CTkButton(self.main_frame, text="Export Report  ",
                                                            image=self.folder_icon, compound="right", anchor="e",
                                                            command=export_file)
        self.report_button_folder.grid(row=4, column=0, padx=10, pady=50, sticky="se")

        # welcome frame button on the bottom main frame
        self.welcome_button = customtkinter.CTkButton(self.main_frame, text="", image=self.profile_icon,
                                                      command=welcome_page_comm, width=30)
        self.welcome_button.grid(row=4, column=1, sticky="se", pady=50)

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
