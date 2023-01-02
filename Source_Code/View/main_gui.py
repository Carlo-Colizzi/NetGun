import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configuration window
        self.title("NetGun")
        self.geometry(f"800x600")

        # variables
        color_option_variable = customtkinter.StringVar(value="System")
        
        def options_settings():
            
            window_options = customtkinter.CTkToplevel()
            window_options.geometry(f"400x200")
            window_options.title("Options")

            def change_mode_appearence(new_mode):
                customtkinter.set_appearance_mode(new_mode)

            # frame options
            frame_options = customtkinter.CTkFrame(window_options, corner_radius=5)
            frame_options.grid(pady=30, padx=30, sticky="nsew")
            frame_options.place(relx=0.5, rely=0.5, anchor="c")

            # color mode set
            color_mode_label = customtkinter.CTkLabel(master=frame_options, text="Color Mode:")
            color_mode_label.grid(row=0, column=0, sticky="w")

            appearence_mode = customtkinter.CTkOptionMenu(master=frame_options, values=["System", "Dark", "Light"], command=change_mode_appearence, variable=color_option_variable)
            appearence_mode.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        # main frame with options and label
        self.main_frame = customtkinter.CTkFrame(self, corner_radius=4)
        self.main_frame.grid(pady=30, padx=30, sticky="nsew")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="c")

        # label
        self.main_frame_label = customtkinter.CTkLabel(self.main_frame, text="NetGun", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.main_frame_label.grid(row=0, column=0, sticky="w")

        # options button
        self.options_button = customtkinter.CTkButton(self.main_frame, text="Options", command=options_settings)
        self.options_button.grid(row=0, column=1, sticky="e")


if __name__ == "__main__":
    app = App()
    app.mainloop()        