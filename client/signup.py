import os
import tkinter as tk
from tkinter import Button, ttk
from PIL import Image, ImageTk
from entry import *
from tkinter import messagebox
from UI import *
class signup(tk.Frame):
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
    data = {"new username": None, "new password": None}
    isBackPage = False
    isSignUp = False
    isInSignUpPage = False
    isError = False
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
        __labelLogo.place(x=66, y=18)
        
        # name page
        __labelName = tk.Label(__wrapper, text="SIGN UP TO SKYCOV", bg = self.__WRAPCOLOR, font = "roboto 20 normal")
        __labelName.place(x=14, y=102)

        # username input
        self.__newusInput = EntryWithPlaceholder(__wrapper, "New Username", "#7d7f8e")
        self.__newusInput.place(x=12, y=138, width=264, height=30)
        # new password input
        self.__newpassInput = EntryWithPlaceholder(__wrapper, "New Password", "#7d7f8e", "yes")
        self.__newpassInput.place(x=12, y=184, width=264, height=30)
        # confirm password input
        self.__confirmPassInput = EntryWithPlaceholder(__wrapper, "Confirm password", "#7d7f8e", "yes")
        self.__confirmPassInput.place(x=12, y=230, width=264, height=30)
        
        # back
        __backButton = tk.Button(__wrapper, text = "Back", 
            bg=self.__BUTTONBGCOLOR, fg=self.__BUTTONFGCOLOR, 
            activebackground=self.__BUTTONBGCOLOR_AC, activeforeground=self.__BUTTONFGCOLOR_AC,
            font=self.__BUTTONFONT)
        __backButton.place(x=12, y=276, width=88, height=36)
        # background on entering widget
        __backButton.bind("<Enter>", func=lambda e: __backButton.config(
        background=self.__BUTTONBGCOLOR_AC, cursor="hand2"))
        # background color on leving widget
        __backButton.bind("<Leave>", func=lambda e: __backButton.config(
        background=self.__BUTTONBGCOLOR))
        # to back page
        __backButton.bind("<Button-1>", func=lambda e: self.toBack())
        
        # sign up
        __signupButton = tk.Button(__wrapper, text = "Sign Up", 
            bg=self.__BUTTONBGCOLOR, fg=self.__BUTTONFGCOLOR, 
            activebackground=self.__BUTTONBGCOLOR_AC, activeforeground=self.__BUTTONFGCOLOR_AC, 
            font=self.__BUTTONFONT)
        __signupButton.place(x=189, y=276, width=88, height=36)
        # background on entering widget
        __signupButton.bind("<Enter>", func=lambda e: __signupButton.config(
            background=self.__BUTTONBGCOLOR_AC, cursor="hand2"))
        # background color on leving widget
        __signupButton.bind("<Leave>", func=lambda e: __signupButton.config(
            background=self.__BUTTONBGCOLOR, cursor="hand2"))
        # read and send data to sign up
        __signupButton.bind("<Button-1>", func=lambda e: self.readAndSend())

    def readAndSend(self):
        if (self.__newusInput.get() != "New Username") and (
            self.__newpassInput.get() != "New Password") and (
            self.__confirmPassInput.get() != "Confirm password"):
            if self.__newpassInput.get() != self.__confirmPassInput.get():
                self.__showWarning()
            else:
                self.isSignUp = True
                self.data["new username"] = str(self.__newusInput.get())
                self.data["new password"] = str(self.__newpassInput.get())

    def toBack(self):
        self.isBackPage = True

    def __showWarning(self):
        __WarningPageBGCOLOR = "#f0f0f0"
        __LabelContentFGCOLOR = "#494b59"
        __LabelErrorFGCOLOR = "#d46600"
        __warning = tk.Toplevel()
        __warning.title("Warning")
        __warning.resizable(width=False, height=False)
        __warning.geometry("256x152")
        __warning.iconbitmap(r"./img/err.ico")

        __frame = tk.Frame(__warning, bg=__WarningPageBGCOLOR)
        __frame.place(x = 0, y = 0, width=256, height=152)

        __labelContent = tk.Label(__warning, text="Oops..", bg=__WarningPageBGCOLOR, 
            fg=__LabelContentFGCOLOR, font="roboto 24 normal")
        __labelContent.place(x=90 ,y=12)

        __labelWarning = tk.Label(__warning, text="Password is not correct!!!",
            bg=__WarningPageBGCOLOR, fg=__LabelErrorFGCOLOR, font="roboto 16 normal")
        __labelWarning.place(x=8 ,y=50)

        # again button
        __againButton = tk.Button(__warning, text = "Try Again", 
            bg=self.__BUTTONBGCOLOR, fg=self.__BUTTONFGCOLOR, 
            activebackground=self.__BUTTONBGCOLOR_AC, activeforeground=self.__BUTTONFGCOLOR_AC, 
            font=self.__BUTTONFONT)
        __againButton.place(x=88, y=95, width=81, height=36)
        # background on entering widget
        __againButton.bind("<Enter>", func=lambda e: __againButton.config(
        background=self.__BUTTONBGCOLOR_AC, cursor="hand2"))
        # background color on leving widget
        __againButton.bind("<Leave>", func=lambda e: __againButton.config(
        background=self.__BUTTONBGCOLOR, cursor="hand2"))
        #close warning
        __againButton.bind("<Button-1>", func=lambda e: __warning.destroy())

    def showErrorSignUP(self):
        self.isError = True
        __ErrorPageBGCOLOR = "#f0f0f0"
        __LabelContentFGCOLOR = "#bb0000"
        pop = tk.Toplevel()
        pop.title("User existed")
        pop.geometry("216x160")
        pop.config(bg=__ErrorPageBGCOLOR)
        pop.iconbitmap(r"./img/err.ico")
        pop.resizable(width = False, height = False)

        __errFrame = tk.Frame(pop, bg = __ErrorPageBGCOLOR)
        __errFrame.place(x = 0, y = 0, width=216, height=160)       

        __labelErrContent = tk.Label(__errFrame, text="User Existed", 
            bg=__ErrorPageBGCOLOR, fg=__LabelContentFGCOLOR, 
            font="roboto 24 normal")
        __labelErrContent.place(x=16 ,y=8)

        __serverDieIcon = Image.open("./img/IDexisted.png")
        __icon = ImageTk.PhotoImage(__serverDieIcon)
        __labelicon = tk.Label(__errFrame, image=__icon, bg=__ErrorPageBGCOLOR)
        __labelicon.image = __icon
        __labelicon.place(x=81 ,y=52)

        # again button
        __againButton = tk.Button(__errFrame, text = "Try Again", 
            bg=self.__BUTTONBGCOLOR, fg=self.__BUTTONFGCOLOR, 
            activebackground=self.__BUTTONBGCOLOR_AC, activeforeground=self.__BUTTONFGCOLOR_AC, 
            font=self.__BUTTONFONT)
        __againButton.place(x=64, y=104, width=81, height=36)
        # background on entering widget
        __againButton.bind("<Enter>", func=lambda e: __againButton.config(
            background=self.__BUTTONBGCOLOR_AC, cursor="hand2"))
        # background color on leving widget
        __againButton.bind("<Leave>", func=lambda e: __againButton.config(
            background=self.__BUTTONBGCOLOR, cursor="hand2"))
        #try agian
        __againButton.bind("<Button-1>", func=lambda e: self.clearError(pop))

    def clearError(self, windows):
        self.isError = False
        windows.destroy()

    def resetSignUp(self):
        self.isQuit = False
        self.isLogin = False
        self.__newusInput.clear()
        self.__newpassInput.clear()
        self.__confirmPassInput.clear()
        