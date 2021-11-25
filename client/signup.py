import os
import tkinter as tk
from tkinter import Button, ttk
from PIL import Image, ImageTk
from entry import *

class signup(tk.Frame):
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

        # logo
        __logoImg = Image.open("./img/logoConnect.png")
        __logo = ImageTk.PhotoImage(__logoImg)
        __labelLogo = tk.Label(__wrapper, image=__logo, bg = __WRAPCOLOR)
        __labelLogo.image = __logo
        __labelLogo.place(x=66, y=18)
        
        # name page
        __labelName = tk.Label(__wrapper, text="SIGN UP TO SKYCOV", bg = __WRAPCOLOR, fg = __NAMEPAGECOLOR, font = "roboto 20 normal")
        __labelName.place(x=14, y=102)

        # username input
        __ipInput = EntryWithPlaceholder(__wrapper, "Username", "#7d7f8e")
        __ipInput.place(x=12, y=138, width=264, height=30)
        # new password input
        __portInput = EntryWithPlaceholder(__wrapper, "Password", "#7d7f8e", "yes")
        __portInput.place(x=12, y=184, width=264, height=30)
        # confirm password input
        __portInput = EntryWithPlaceholder(__wrapper, "Confirm password", "#7d7f8e", "yes")
        __portInput.place(x=12, y=230, width=264, height=30)
        
        # sign up
        __signupButton = tk.Button(__wrapper, text = "Sign Up", bg=__BUTTONBGCOLOR, fg=__BUTTONFGCOLOR, activebackground=__BUTTONBGCOLOR_AC, activeforeground=__BUTTONFGCOLOR_AC, font=__BUTTONFONT)
        __signupButton.place(x=173, y=276, width=103, height=36)
        # background on entering widget
        __signupButton.bind("<Enter>", func=lambda e: __signupButton.config(
        background=__BUTTONBGCOLOR_AC, cursor="hand2"))
        # background color on leving widget
        __signupButton.bind("<Leave>", func=lambda e: __signupButton.config(
        background=__BUTTONBGCOLOR, cursor="hand2"))