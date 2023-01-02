import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # configuration window
        self.title("NetGun")
        self.geometry(f"1200x600")

        # variables
        color_option_variable = customtkinter.StringVar(value="System")
        ip_var = customtkinter.StringVar(value="IP address")
        port_var = customtkinter.StringVar(value="Port")
        tcp_udp_var = customtkinter.StringVar(value="TCP-UDP")
        type_adv_var = customtkinter.StringVar(value="Advanced")
        scan_type_var = customtkinter.StringVar(value="Shallow")

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

        # main frame with options and label
        self.main_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(pady=15, padx=15, sticky="nsew")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="c")

        # label
        self.main_frame_label = customtkinter.CTkLabel(self.main_frame, text="NetGun", font=customtkinter.CTkFont(size=25, weight="bold"))
        self.main_frame_label.grid(row=0, column=0, sticky="nw")

        # options button
        self.options_button = customtkinter.CTkButton(self.main_frame, text="Options", command=options_settings)
        self.options_button.grid(row=0, column=2, sticky="e")

        # buttons and text in main
        # set the frame first
        self.center_frame = customtkinter.CTkFrame(self.main_frame)
        self.center_frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)

        # placeholders entry
        self.ip_entry = customtkinter.CTkEntry(master=self.center_frame, placeholder_text="IP Address", textvariable=ip_var)
        self.ip_entry.grid(row=0, column=0, sticky="w", padx=10)

        self.port_entry = customtkinter.CTkEntry(master=self.center_frame, placeholder_text="Port", textvariable=port_var)
        self.port_entry.grid(row=0, column=1, sticky="w", padx=10)

        # option menus
        self.tcp_udp_option = customtkinter.CTkOptionMenu(master=self.center_frame, values=["TCP", "UDP", "TCP-UDP"], variable=tcp_udp_var)
        self.tcp_udp_option.grid(row=0, column=2, sticky="w", padx=10)

        self.type_adv_option = customtkinter.CTkOptionMenu(master=self.center_frame, values=["Base", "Advanced"], variable=type_adv_var)
        self.type_adv_option.grid(row=0, column=3, sticky="w", padx=10)

        self.scan_type_option = customtkinter.CTkOptionMenu(master=self.center_frame, values=["Shallow", "Deep"], variable=scan_type_var)
        self.scan_type_option.grid(row=0, column=4, sticky="w", padx=10)

        # button scan
        self.scan_button = customtkinter.CTkButton(self.center_frame, text="Scan", width=70, height=25)
        self.scan_button.grid(row=0, column=5, sticky="nsew")

if __name__ == "__main__":
    app = App()
    app.mainloop()        