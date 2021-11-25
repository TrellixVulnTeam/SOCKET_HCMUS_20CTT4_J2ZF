import os
import tkinter as tk
from tkinter import Button, ttk
from PIL import Image, ImageTk
from entry import *

class turnup(tk.Frame):
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
        __RESULTCOLOR = "#7d7f8e"
        __NAMEPAGECOLOR = "#494b59"

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

        # wrapper
        __wrapper = tk.Frame(self, bg = __WRAPCOLOR)
        __wrapper.place(x = 16, y = 16, width=288, height=328)

        # user account
        __account = tk.Frame(__wrapper, bg = __WRAPCOLOR)
        __account.place(x = 20, y = 16, width=180, height=34)
        # avatar
        __avtImg = Image.open("./img/avatar.png")
        __avatar = ImageTk.PhotoImage(__avtImg)
        __labelAvatar = tk.Label(__account, image=__avatar, bg = __WRAPCOLOR)
        __labelAvatar.image = __avatar
        __labelAvatar.place(x=0, y=0)
        
        __labelUsername = tk.Label(__account, text="hcmusMMT2012", bg = __WRAPCOLOR, fg=__NAMEPAGECOLOR, font = "roboto 13 normal")
        __labelUsername.place(x=40, y=6)

        # log out
        __logouButton = tk.Button(__wrapper, text = "Log Out", bg=__BUTTONBGCOLOR, fg=__BUTTONFGCOLOR, activebackground=__BUTTONBGCOLOR_AC, activeforeground=__BUTTONFGCOLOR_AC, font=__BUTTONFONT)
        __logouButton.place(x=198, y=16, width=72, height=36)
        # background on entering widget
        __logouButton.bind("<Enter>", func=lambda e: __logouButton.config(
        background=__BUTTONBGCOLOR_AC, foreground=__BUTTONFGCOLOR_AC, cursor="hand2"))
        # background color on leving widget
        __logouButton.bind("<Leave>", func=lambda e: __logouButton.config(
        background=__BUTTONBGCOLOR, foreground=__BUTTONFGCOLOR, cursor="hand2"))

        # name page
        __labelName = tk.Label(__wrapper, text="TURN UP", bg = __WRAPCOLOR, fg=__NAMEPAGECOLOR, font = "roboto 20 normal")
        __labelName.place(x=94, y=92)

        # query input
        __queryInput = EntryWithPlaceholder(__wrapper, "Province or City", "#7d7f8e")
        __queryInput.place(x=23, y=154, width=172, height=30)
        
        # search
        __iconSearch = tk.PhotoImage(file="./img/search.png")
        __searchButton = tk.Button(__wrapper, image=__iconSearch, bg=__BUTTONBGCOLOR, activebackground=__BUTTONBGCOLOR_AC, font=__BUTTONFONT)
        __searchButton.place(x=207, y=152, width=64, height=36)
        # background on entering widget
        __searchButton.bind("<Enter>", func=lambda e: __searchButton.config(
        image=__iconSearch, background=__BUTTONBGCOLOR_AC, cursor="hand2"))
        # background color on leving widget
        __searchButton.bind("<Leave>", func=lambda e: __searchButton.config(
        image=__iconSearch, background=__BUTTONBGCOLOR, cursor="hand2"))

        # result
        __labelResult = tk.Label(__wrapper, text="The current number of cases in QN is 999", bg = __WRAPCOLOR, fg = __RESULTCOLOR, font = "roboto 10 normal")
        __labelResult.place(x=22, y=222)