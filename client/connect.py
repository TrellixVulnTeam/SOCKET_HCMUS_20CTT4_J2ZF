import os
import tkinter as tk
from tkinter import Button, ttk
from PIL import Image, ImageTk
from entry import *
from tkinter import messagebox
class connect(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        __HEIGHT = 360
        __WIDTH = 640
        __BGCOLOR = "#fcfafa"
        __BUTTONBGCOLOR = "#0b0d1a"
        __BUTTONFGCOLOR = "#cecfd1"
        __BUTTONBGCOLOR_AC = "#5c5e6b"
        __BUTTONFGCOLOR_AC = "#ffffff"
        __BUTTONFONT = "roboto 11 bold"
        __BGENTRY = "#fafafa"
        __FGENTRY = "#f5f5f5"
        __WRAPCOLOR = "#f0f0f0"
        __ERRORFLOATINGCOLOR = "#0b0d1a"

        __style = ttk.Style()
        __style.configure('My.TFrame', background=__BGCOLOR)
        self = ttk.Frame(self, style='My.TFrame')
        self.place(height=__HEIGHT, width=__WIDTH, x = 0, y = 0)
        self.config()

        __bannerImg = Image.open("./img/clientBanner.png")
        __banner = ImageTk.PhotoImage(__bannerImg)
        __labelImg = tk.Label(self, image=__banner, bg = __BGCOLOR)
        __labelImg.image = __banner
        __labelImg.place(x=__WIDTH/2, y=0)

        __wrapper = tk.Frame(self, bg = __WRAPCOLOR)
        __wrapper.place(x = 16, y = 16, width=288, height=328)

        __logoImg = Image.open("./img/logoConnect.png")
        __logo = ImageTk.PhotoImage(__logoImg)
        __labelLogo = tk.Label(__wrapper, image=__logo, bg = __WRAPCOLOR)
        __labelLogo.image = __logo
        __labelLogo.place(x=66, y=40)
        
        __ipInput = EntryWithPlaceholder(__wrapper, "IP address", "#7d7f8e")
        __ipInput.place(x=12, y=124, width=264, height=30)
        __portInput = EntryWithPlaceholder(__wrapper, "PORT", "#7d7f8e")
        __portInput.place(x=12, y=170, width=264, height=30)
        
        # connect button
        __connectButton = tk.Button(__wrapper, text = "Connect To Server", bg=__BUTTONBGCOLOR, fg=__BUTTONFGCOLOR, activebackground=__BUTTONBGCOLOR_AC, activeforeground=__BUTTONFGCOLOR_AC, font=__BUTTONFONT)
        __connectButton.place(x=60, y=216, width=173, height=36)

        # background on entering widget
        __connectButton.bind("<Enter>", func=lambda e: __connectButton.config(
        background=__BUTTONBGCOLOR_AC, cursor="hand2"))
  
        # background color on leving widget
        __connectButton.bind("<Leave>", func=lambda e: __connectButton.config(
        background=__BUTTONBGCOLOR))

        

