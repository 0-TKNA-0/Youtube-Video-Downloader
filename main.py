import customtkinter as ctk
from pytube import YouTube 
from PIL import Image, ImageTk

try: # ONLY WORKS ON WINDOWS SO EXCEPTION HANDLING FOR OTHER OS SYSTEMS
    from ctypes import windll, byref, sizeof, c_int # required to change title bar colour
except:
    pass

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configured Window Settings
        self.title("")
        self.iconbitmap("empty.ico")
        self.geometry("1200x600")
        self.resizable(False,False)
        self.config(background = "#374A67")

        self.mainloop()

App()