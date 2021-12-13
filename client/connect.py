import os
import tkinter as tk
from tkinter import Button, ttk
from PIL import Image, ImageTk
from entry import *
from tkinter import messagebox
from UI import *
class connect(tk.Frame):
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
    data =  {"ip": None}
    isError = False
    isInConnectPage = False

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.primaryFrame = tk.Frame(parent, bg=self.__BGCOLOR)
        self.primaryFrame.place(height=self.__HEIGHT, width=self.__WIDTH, x = 0, y = 0)

        __bannerImg = Image.open("./img/clientBanner.png")
        __banner = ImageTk.PhotoImage(__bannerImg)
        __labelImg = tk.Label(self.primaryFrame, image=__banner, bg = self.__BGCOLOR)
        __labelImg.image = __banner
        __labelImg.place(x=self.__WIDTH/2, y=0)

        __wrapper = tk.Frame(self.primaryFrame, bg = self.__WRAPCOLOR)
        __wrapper.place(x = 16, y = 16, width=288, height=328)

        __logoImg = Image.open("./img/logoConnect.png")
        __logo = ImageTk.PhotoImage(__logoImg)
        __labelLogo = tk.Label(__wrapper, image=__logo, bg = self.__WRAPCOLOR)
        __labelLogo.image = __logo
        __labelLogo.place(x=66, y=40)
        
        self.__ipInput = EntryWithPlaceholder(__wrapper, "IP address", "#7d7f8e")
        self.__ipInput.place(x=12, y=140, width=264, height=30)

         # connect button
        __connectButton = tk.Button(__wrapper, text = "Connect To Server", bg=self.__BUTTONBGCOLOR, fg=self.__BUTTONFGCOLOR, activebackground=self.__BUTTONBGCOLOR_AC, activeforeground=self.__BUTTONFGCOLOR_AC, font=self.__BUTTONFONT)
        __connectButton.place(x=60, y=196, width=173, height=36)
        __connectButton.bind("<Enter>", func=lambda e: __connectButton.config(
        background=self.__BUTTONBGCOLOR_AC, cursor="hand2"))
        __connectButton.bind("<Leave>", func=lambda e: __connectButton.config(
        background=self.__BUTTONBGCOLOR))
        # clicked to send data
        __connectButton.bind("<Button-1>", func=lambda e: self.readAndSend())
    
    #read data from entry
    def readAndSend(self):
        if self.__ipInput.get() != "IP address":
            self.data["ip"] = str(self.__ipInput.get())
    
    def showErrConnection(self):
        # change isError
        self.isError = True
        # show UI error
        __ErrorPageBGCOLOR = "#f0f0f0"
        __LabelContentFGCOLOR = "#494b59"
        __LabelErrorFGCOLOR = "#bb0000"
        self.__errWindows = tk.Toplevel()
        self.__errWindows.title("Error")
        self.__errWindows.geometry("180x147")
        self.__errWindows.config(bg=__ErrorPageBGCOLOR)
        self.__errWindows.iconbitmap(r"./img/err.ico")
        self.__errWindows.resizable(width = False, height = False)

        __errFrame = tk.Frame(self.__errWindows, bg = __ErrorPageBGCOLOR)
        __errFrame.place(x = 0, y = 0, width=180, height=147)       

        __labelErrContent = tk.Label(__errFrame, text="Oops..", 
            bg=__ErrorPageBGCOLOR, fg=__LabelContentFGCOLOR, 
            font="roboto 24 normal")
        __labelErrContent.place(x=45 ,y=20)

        __labelErr = tk.Label(__errFrame, text="404 Not Found", 
            bg=__ErrorPageBGCOLOR, fg=__LabelErrorFGCOLOR, 
            font="roboto 16 normal")
        __labelErr.place(x=18 ,y=55)

        # again button
        __againButton = tk.Button(__errFrame, text = "Try Again", 
            bg=self.__BUTTONBGCOLOR, fg=self.__BUTTONFGCOLOR, 
            activebackground=self.__BUTTONBGCOLOR_AC, activeforeground=self.__BUTTONFGCOLOR_AC, 
            font=self.__BUTTONFONT)
        __againButton.place(x=49, y=95, width=81, height=36)
        # background on entering widget
        __againButton.bind("<Enter>", func=lambda e: __againButton.config(
            background=self.__BUTTONBGCOLOR_AC, cursor="hand2"))
        # background color on leving widget
        __againButton.bind("<Leave>", func=lambda e: __againButton.config(
            background=self.__BUTTONBGCOLOR, cursor="hand2"))
        #try agian
        __againButton.bind("<Button-1>", func=lambda e: self.tryAgain(self.__errWindows))

        self.__errWindows.protocol("WM_DELETE_WINDOW", self.closePop)

    def tryAgain(self, windows):
        self.isError = False
        self.data["ip"] = None
        self.__ipInput.delete('0', 'end')
        windows.destroy()
    
    def closePop(self):
        self.isError = False
        self.data["ip"] = None
        self.__errWindows.destroy()