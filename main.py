import customtkinter as ctk
from pytube import YouTube 
from PIL import Image, ImageTk
from settings import *

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

        # changes the title bar colour
        self.changeTitleBarColour()

        # Gridded Layout
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 2)

        TopFrame(self)


        self.mainloop()

        # Changes the colour of the title bar
    def changeTitleBarColour(self):
        try: # ONLY WORKS ON WINDOWS SO EXCEPTION HANDLING FOR OTHER OS SYSTEMS
            # Change title bar colour
            HWND = windll.user32.GetParent(self.winfo_id())
            windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(titleBarHexColour)), sizeof(c_int)) # 35 = title bar colour attribute
        except:
            pass


class TopFrame(ctk.CTkFrame):
    def __init__(self, parent):
        # text attributes
        headerFont = ctk.CTkFont(family = font, size = headerTextSize, weight = "bold")
        super().__init__(master = parent, corner_radius = buttonCornerRadius)
        self.grid(row = 0, column = 0, sticky = "nsew", padx = 10, pady = 10)

        header = ctk.CTkLabel(
            master = self,
            text = "YouTube Video Downloader", 
            font = headerFont, 
            text_color = white)
        header.pack(fill = "both", expand = True, padx = 5, pady = 5)


App()