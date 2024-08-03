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

        # data
        switch_toggle = "dark"

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

        light_image = ctk.CTkImage(Image.open("light.png"), size=(30,30))
        dark_image = ctk.CTkImage(Image.open("dark.png"), size=(30,30))

        super().__init__(master = parent, corner_radius = buttonCornerRadius, bg_color = "#374A67")
        self.grid(row = 0, column = 0, sticky = "nsew", padx = 10, pady = 10)

        self.dark_button = ctk.CTkButton(
            self,
            width=35,
            height=35,
            text="",
            image=dark_image,
            font=("Ubuntu", 15, "bold"),
            fg_color=("#374A67"),
            command=self.dark_mode)
        self.dark_button.pack(side = "right", anchor = "ne", padx = 10, pady = 10, fill = "both")

        self.header = ctk.CTkLabel(
            master = self,
            text = "YouTube Video Downloader", 
            font = headerFont, 
            text_color = white)
        self.header.pack(fill = "both", expand = True, padx = 5, pady = 5, )


        self.light_button = ctk.CTkButton(
            self,
            width=35,
            height=35,
            text="",
            image=light_image,
            font=("Ubuntu", 15, "bold"),
            fg_color=("#374A67"),
            command=self.light_mode)


    def light_mode(self):
        global switch_toggle
        ctk.set_appearance_mode("light")
        switch_toggle = "light"
        self.configure( fg_color ="white")
        
        self.light_button.pack_forget()
        self.header.pack_forget()
        self.dark_button.pack(side = "right", anchor = "ne", padx = 10, pady = 10, fill = "both")
        self.header.pack(fill = "both", expand = True, padx = 5, pady = 5)

    def dark_mode(self):
        global switch_toggle
        ctk.set_appearance_mode("dark")
        switch_toggle = "dark"
        self.configure(fg_color ="#374A67")

        self.dark_button.pack_forget()
        self.header.pack_forget()
        self.light_button.pack(side = "right", anchor = "ne", padx = 10, pady = 10, fill = "both")
        self.header.pack(fill = "both", expand = True, padx = 5, pady = 5)


App()