import os
import tkinter as tk
from tkinter import Button, ttk
from PIL import Image, ImageTk
from entry import *
from tkinter import messagebox
from UI import *
class login(tk.Frame):
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
    data = {"username": None, "password": None}
    isToSignUp = False
    isLogin = False
    isQuit = False

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
        __wrapper.place(x = 16, y = 16, width=288, height=272)

        __logoImg = Image.open("./img/logoConnect.png")
        __logo = ImageTk.PhotoImage(__logoImg)
        __labelLogo = tk.Label(__wrapper, image=__logo, bg = self.__WRAPCOLOR)
        __labelLogo.image = __logo
        __labelLogo.place(x=66, y=20)
        
        # name page
        __labelName = tk.Label(__wrapper, text="LOG IN TO SKYCOV", bg = self.__WRAPCOLOR, font = "roboto 20 normal")
        __labelName.place(x=23, y=92)

        # username input
        self.__usInput = EntryWithPlaceholder(__wrapper, "Username", "#7d7f8e")
        self.__usInput.place(x=12, y=138, width=264, height=30)
        # password input
        self.__passInput = EntryWithPlaceholder(__wrapper, "Password", "#7d7f8e", "yes")
        self.__passInput.place(x=12, y=182, width=264, height=30)

        # sign up
        __signupButton = tk.Button(__wrapper, text = "Sign Up", 
            bg=self.__BUTTONBGCOLOR, fg=self.__BUTTONFGCOLOR, 
            activebackground=self.__BUTTONBGCOLOR_AC, activeforeground=self.__BUTTONFGCOLOR_AC, 
            font=self.__BUTTONFONT)
        __signupButton.place(x=12, y=228, width=88, height=36)
        # background on entering widget
        __signupButton.bind("<Enter>", func=lambda e: __signupButton.config(
            background=self.__BUTTONBGCOLOR_AC, cursor="hand2"))
        # background color on leving widget
        __signupButton.bind("<Leave>", func=lambda e: __signupButton.config(
            background=self.__BUTTONBGCOLOR))
        # to Sign Up page
        __signupButton.bind("<Button-1>", func=lambda e: self.toSignUp())

        # log in
        __loginButton = tk.Button(__wrapper, text = "Log in", 
            bg=self.__BUTTONBGCOLOR, fg=self.__BUTTONFGCOLOR, 
            activebackground=self.__BUTTONBGCOLOR_AC, activeforeground=self.__BUTTONFGCOLOR_AC, 
            font=self.__BUTTONFONT)
        __loginButton.place(x=189, y=228, width=88, height=36)
        # background on entering widget
        __loginButton.bind("<Enter>", func=lambda e: __loginButton.config(
            background=self.__BUTTONBGCOLOR_AC, cursor="hand2"))
        # background color on leving widget
        __loginButton.bind("<Leave>", func=lambda e: __loginButton.config(
            background=self.__BUTTONBGCOLOR, cursor="hand2"))
        # get and send data to log in
        __loginButton.bind("<Button-1>", func=lambda e: self.readAndSend())

        # quit
        __quitButton = tk.Button(self.primaryFrame, text = "Quit", 
            bg=self.__BUTTONBGCOLOR, fg=self.__BUTTONFGCOLOR, 
            activebackground=self.__BUTTONBGCOLOR_AC, activeforeground=self.__BUTTONFGCOLOR_AC, 
            font=self.__BUTTONFONT)
        __quitButton.place(x=256, y=300, width=48, height=36)
        # background on entering widget
        __quitButton.bind("<Enter>", func=lambda e: __quitButton.config(
            background=self.__BUTTONBGCOLOR_AC, cursor="hand2"))
        # background color on leving widget
        __quitButton.bind("<Leave>", func=lambda e: __quitButton.config(
            background=self.__BUTTONBGCOLOR, cursor="hand2"))
        # get and send data to log in
        __quitButton.bind("<Button-1>", func=lambda e: self.toQuit())

    #read data from entry
    def readAndSend(self):
        if (self.__usInput.get() != "Username" and self.__passInput.get() != "Password") or (
            self.__usInput.get() != "" and self.__passInput.get() != ""):
            self.isLogin = True
            self.data["username"] = str(self.__usInput.get())
            self.data["password"] = str(self.__passInput.get())
        else:
            self.showErrSyntaxLogIn()
    
    def toSignUp(self):
        self.isToSignUp = True

    def toQuit(self):
        __WarningPageBGCOLOR = "#f0f0f0"
        __LabelContentFGCOLOR = "#494b59"
        __LabelErrorFGCOLOR = "#d46600"
        __warning = tk.Toplevel()
        __warning.title("Confirm")
        __warning.resizable(width=False, height=False)
        __warning.geometry("256x152")
        __warning.iconbitmap(r"./img/err.ico")

        __frame = tk.Frame(__warning, bg=__WarningPageBGCOLOR)
        __frame.place(x = 0, y = 0, width=256, height=152)

        __labelContent = tk.Label(__warning, text="Oops..", bg=__WarningPageBGCOLOR, 
            fg=__LabelContentFGCOLOR, font="roboto 24 normal")
        __labelContent.place(x=90 ,y=12)

        __labelWarning = tk.Label(__warning, text="Are you sure about that?",
            bg=__WarningPageBGCOLOR, fg=__LabelErrorFGCOLOR, font="roboto 16 normal")
        __labelWarning.place(x=14 ,y=50)

        # Yes button
        __yesButton = tk.Button(__warning, text = "Yes", 
            bg=self.__BUTTONBGCOLOR, fg=self.__BUTTONFGCOLOR, 
            activebackground=self.__BUTTONBGCOLOR_AC, activeforeground=self.__BUTTONFGCOLOR_AC, 
            font=self.__BUTTONFONT)
        __yesButton.place(x=138, y=95, width=81, height=36)
        # background on entering widget
        __yesButton.bind("<Enter>", func=lambda e: __yesButton.config(
        background=self.__BUTTONBGCOLOR_AC, cursor="hand2"))
        # background color on leving widget
        __yesButton.bind("<Leave>", func=lambda e: __yesButton.config(
        background=self.__BUTTONBGCOLOR, cursor="hand2"))
        #close warning
        __yesButton.bind("<Button-1>", func=lambda e: self.QuitConfirm(__warning))

        # No button
        __noButton = tk.Button(__warning, text = "No", 
            bg=self.__BUTTONBGCOLOR, fg=self.__BUTTONFGCOLOR, 
            activebackground=self.__BUTTONBGCOLOR_AC, activeforeground=self.__BUTTONFGCOLOR_AC, 
            font=self.__BUTTONFONT)
        __noButton.place(x=36, y=95, width=81, height=36)
        # background on entering widget
        __noButton.bind("<Enter>", func=lambda e: __noButton.config(
        background=self.__BUTTONBGCOLOR_AC, cursor="hand2"))
        # background color on leving widget
        __noButton.bind("<Leave>", func=lambda e: __noButton.config(
        background=self.__BUTTONBGCOLOR, cursor="hand2"))
        #close warning
        __noButton.bind("<Button-1>", func=lambda e: __warning.destroy())

    def QuitConfirm(self, windows):
        self.isQuit = True
        windows.destroy()

    def showErrSyntaxLogIn(self):
        __ErrorPageBGCOLOR = "#f0f0f0"
        __LabelContentFGCOLOR = "#494b59"
        __LabelErrorFGCOLOR = "#bb0000"
        pop = tk.Toplevel()
        pop.title("LogIn Failed")
        pop.geometry("180x147")
        pop.config(bg=__ErrorPageBGCOLOR)
        pop.iconbitmap(r"./img/err.ico")
        pop.resizable(width = False, height = False)

        __errFrame = tk.Frame(pop, bg = __ErrorPageBGCOLOR)
        __errFrame.place(x = 0, y = 0, width=180, height=147)       

        __labelErrContent = tk.Label(__errFrame, text="Oops..", 
            bg=__ErrorPageBGCOLOR, fg=__LabelContentFGCOLOR, 
            font="roboto 24 normal")
        __labelErrContent.place(x=45 ,y=20)

        __labelErr = tk.Label(__errFrame, text="User Not Found", 
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
        __againButton.bind("<Button-1>", func=lambda e: __errFrame.destroy())

    def showWrongLogIn(self):
        __ErrorPageBGCOLOR = "#f0f0f0"
        __LabelContentFGCOLOR = "#bb0000"
        pop = tk.Toplevel()
        pop.title("Error")
        pop.geometry("216x160")
        pop.config(bg=__ErrorPageBGCOLOR)
        pop.iconbitmap(r"./img/err.ico")
        pop.resizable(width = False, height = False)

        __errFrame = tk.Frame(pop, bg = __ErrorPageBGCOLOR)
        __errFrame.place(x = 0, y = 0, width=216, height=160)       

        __labelErrContent = tk.Label(__errFrame, text="Wrong !!!", 
            bg=__ErrorPageBGCOLOR, fg=__LabelContentFGCOLOR, 
            font="roboto 24 normal")
        __labelErrContent.place(x=40 ,y=8)

        __serverDieIcon = Image.open("./img/wrongPass.png")
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
        __againButton.bind("<Button-1>", func=lambda e: pop.destroy())
 