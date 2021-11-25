import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class login(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        __HEIGHT = 360
        __WIDTH = 640
        __BGCOLOR = "#fcfafa"
        __style = ttk.Style()
        __style.configure('My.TFrame', background=__BGCOLOR)
        self = ttk.Frame(self, style='My.TFrame')
        self.place(height=__HEIGHT, width=__WIDTH, x = 0, y = 0)
        self.config()

        __bannerImg = Image.open("./img/clientBanner.png")
        __banner = ImageTk.PhotoImage(__bannerImg)
        __labelImg = tk.Label(self, image=__banner, background=__BGCOLOR)
        __labelImg.image = __banner
        __labelImg.place(x=__WIDTH/2, y=0)
    
        __logoImg = Image.open("./img/logoConnect.png")
        __logo = ImageTk.PhotoImage(__logoImg)
        __labelLogo = tk.Label(self, image=__logo, bg = __BGCOLOR)
        __labelLogo.image = __logo
        __labelLogo.place(x=82, y=56)   