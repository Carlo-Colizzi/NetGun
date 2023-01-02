import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configurazione window
        self.title("NetGun")
        self.geometry(f"800x600")
        
        # frame con titolo e pulsante opzioni
        self.main_frame = customtkinter.CTkFrame(self, corner_radius=1)

if __name__ == "__main__":
    app = App()
    app.mainloop()        