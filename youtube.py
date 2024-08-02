import customtkinter
from pytube import YouTube 
from PIL import Image, ImageTk

window = customtkinter.CTk()
window.title("Youtube Video Downloader")
window.geometry("800x700")
window.config(background="#374A67")
window.resizable(False,False)

switch_toggle = "dark"

light_image = customtkinter.CTkImage(Image.open("light.png"), size=(30,30))
dark_image = customtkinter.CTkImage(Image.open("dark.png"), size=(30,30))


# This section creates 2 functions that allow the light and dark mode buttons to switch between there corresponding modes
def light_mode():
    global switch_toggle
    customtkinter.set_appearance_mode("light")
    switch_toggle = "light"
    window.config(background="white")
    
    light_button.place_forget()
    dark_button.place(x=700, y=35)

def dark_mode():
    global switch_toggle
    customtkinter.set_appearance_mode("dark")
    switch_toggle = "dark"
    window.config(background="#374A67")

    dark_button.place_forget()
    light_button.place(x=700, y=35)

def downloadevent():
    try:
        youtubeURL = youtubeURL_entry.get()
        youtubeObject = YouTube(youtubeURL)
        video = youtubeObject.streams.get_highest_resolution()
        video.download()



    except:
        error_label = customtkinter.CTkLabel(
            inputframe,
            text="Invalid URL",
            font=("Ubuntu", 12, "bold"),
            text_color="red",
            width=100,
            height=20,
            corner_radius=10)
        error_label.place(x=275, y=110)
        
        inputframe.after(3000, lambda: error_label.destroy())
    
    finishedDownload_Label.configure(text="Download Complete")
    inputframe.after(3000, lambda: finishedDownload_Label.destroy())
    
# This section contains all of the parameters for each widget and packs / places them on the window
framebar = customtkinter.CTkFrame(
    window,
    width=800,
    height=100,
    fg_color="#0E1116")
framebar.pack()

# Frame that hides behind the input frame to cover up white conflicting background when rounding corners 
hidingframe = customtkinter.CTkFrame(
    window,
    width=700,
    height=225,
    fg_color=("white", "#374A67"))
hidingframe.pack(pady = 50)


inputframe = customtkinter.CTkFrame(
    hidingframe,
    width=650,
    height=300,
    corner_radius= 20,
    fg_color="#0E1116")
inputframe.pack()


youtubeDownloader_Label = customtkinter.CTkLabel(
    framebar, 
    text = "Download Youtube\nVideos",
    font = ("Ubuntu", 30, "bold"),    
    text_color = "white",
    width=800,
    height=100,
    corner_radius = 10)
youtubeDownloader_Label.pack()


instructionURL_Label = customtkinter.CTkLabel(
    inputframe, 
    text = "Enter A Youtube URL Below",
    font = ("Ubuntu", 20, "bold"),    
    text_color = "white",
    width=100,
    height=40,
    corner_radius = 10)
instructionURL_Label.place(x=190, y=10)


finishedDownload_Label = customtkinter.CTkLabel(
    inputframe, 
    text = "",
    font = ("Ubuntu", 15, "bold"),    
    text_color = "white",
    width=100,
    height=40,
    corner_radius = 10)
finishedDownload_Label.place(x=250, y=100)


youtubeURL_entry = customtkinter.CTkEntry(
    inputframe,
    font=("Ubuntu", 15, "bold"),
    width=500,
    height=40,
    placeholder_text="                                        www.youtube.com/watch")
youtubeURL_entry.place(x=75, y=65)


dark_button = customtkinter.CTkButton(
    framebar,
    width=35,
    height=35,
    text="",
    image=dark_image,
    font=("Ubuntu", 15, "bold"),
    fg_color=("#374A67"),
    command=dark_mode)
dark_button.place(x=700, y=35)


light_button = customtkinter.CTkButton(
    framebar,
    width=35,
    height=35,
    text="",
    image=light_image,
    font=("Ubuntu", 15, "bold"),
    fg_color=("#374A67"),
    command=light_mode)
light_button.place(x=700, y=35)

download_button = customtkinter.CTkButton(
    inputframe, 
    text="Download",
    width= 200,
    height= 45,
    font=("Ubuntu", 20, "bold"),
    fg_color=("#616283"),
    command=downloadevent)
download_button.place(x=225, y=215)


window.mainloop()