import tkinter as tk
from tkinter import Frame, Toplevel, Widget, ttk
from PIL import Image, ImageTk
from connect import *
from login import *
from signup import *
from turnup import *
from clientSoc import *

class App(tk.Tk):
    # client Socket
    clientSock = clientSocket()

    # UI constant
    __BGCOLOR = "#ffffff"
    __TITLE = "SkyCov Client"
    __FAVICON = r"./img/favicon.ico"
    __HEIGHT = 360
    __WIDTH = 640
    __BUTTONBGCOLOR = "#0b0d1a"
    __BUTTONFGCOLOR = "#cecfd1"
    __BUTTONBGCOLOR_AC = "#5c5e6b"
    __BUTTONFGCOLOR_AC = "#ffffff"
    __BUTTONFONT = "roboto 11 bold"
    isError = False

    # name page
    CONNECTPAGE = "connect"
    LOGINPAGE = "log in"
    SIGNUPPAGE = "sign up"
    TURNUPPAGE = "turn up"
    def __init__(self):
        tk.Tk.__init__(self)
        self.initUI()

    def run(self):
        self.mainloop()

    def initUI(self):
        self.geometry(str(self.__WIDTH) + "x" + str(self.__HEIGHT))
        self.title(self.__TITLE)
        self.iconbitmap(self.__FAVICON)
        self.resizable(width = False, height = False)

        # screen layer
        self.__screen = tk.Frame()
        self.__screen.configure(background="#fafafa")

        self.__screen.pack(side="top", fill="both", expand=True)
        self.__screen.grid_rowconfigure(0, weight=1)
        self.__screen.grid_columnconfigure(0, weight=1)

        self.layerFrames = {}
        for fr in (connect, login, signup, turnup):
            frame = fr(self.__screen, self.clientSock, self)
            frame.grid(row = 0, column = 0, sticky = "nsew")
            self.layerFrames[fr] = frame

        self.layerFrames[connect].primaryFrame.tkraise()

    def showUpPage(self, framePage):
        if framePage == self.CONNECTPAGE: 
            self.layerFrames[connect].primaryFrame.tkraise()
        elif framePage == self.LOGINPAGE:
            self.layerFrames[login].primaryFrame.tkraise()
        elif framePage == self.SIGNUPPAGE:
            self.layerFrames[signup].primaryFrame.tkraise()
        elif framePage == self.TURNUPPAGE:
            self.layerFrames[turnup].primaryFrame.tkraise()

        

    def showError(self):
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

        __labelErrContent = tk.Label(__errFrame, text="Server die :(", 
            bg=__ErrorPageBGCOLOR, fg=__LabelContentFGCOLOR, 
            font="roboto 24 normal")
        __labelErrContent.place(x=20 ,y=8)

        __serverDieIcon = Image.open("./img/iconSerDie.png")
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
        self.isError = True
        windows.destroy()

    def changeAccountName(self, name):
        self.layerFrames[turnup].changeACN(name)

def main():
    ui = App()
    ui.run()

if __name__ == "__main__":
    main()