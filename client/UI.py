import tkinter as tk
from tkinter import Frame, Toplevel, Widget, ttk
from PIL import Image, ImageTk
from connect import *
from login import *
from signup import *
from turnup import *


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.__BGCOLOR = "#ffffff"
        self.__TITLE = "SkyCov Client"
        self.__FAVICON = r"./img/favicon.ico"
        self.__HEIGHT = 360
        self.__WIDTH = 640
        self.initUI()
        self.showError()
        # self.showUpPage(turnup)
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
            frame = fr(self.__screen)
            frame.grid(row = 0, column = 0, sticky = "nsew")
            self.layerFrames[fr] = frame

        self.layerFrames[connect].tkraise()

    def showUpPage(self, frameClass):
        self.layerFrames[frameClass].tkraise()

    def showError(self):
        popPageBGCOLOR = "#f0f0f0"
        labelContentFGCOLOR = "#494b59"
        labelErrorFGCOLOR = "#bb0000"
        __BUTTONBGCOLOR = "#0b0d1a"
        __BUTTONFGCOLOR = "#cecfd1"
        __BUTTONBGCOLOR_AC = "#5c5e6b"
        __BUTTONFGCOLOR_AC = "#ffffff"
        __BUTTONFONT = "roboto 11 bold"
        global pop
        pop = Toplevel(self)
        pop.title("Error")
        pop.geometry("180x147")
        pop.config(bg=popPageBGCOLOR)
        pop.iconbitmap(r"./img/err.ico")
        pop.resizable(width = False, height = False)

        popFrame = tk.Frame(pop, bg = popPageBGCOLOR)
        popFrame.place(x = 0, y = 0, width=180, height=147)       

        labelErr = tk.Label(popFrame, text="Oops..", bg=popPageBGCOLOR, fg=labelContentFGCOLOR, font="roboto 24 normal")
        labelErr.place(x=45 ,y=20)

        labelErr = tk.Label(popFrame, text="404 Not Found", bg=popPageBGCOLOR, fg=labelErrorFGCOLOR, font="roboto 16 normal")
        labelErr.place(x=18 ,y=55)

        # again button
        againButton = tk.Button(popFrame, text = "Try Again", bg=__BUTTONBGCOLOR, fg=__BUTTONFGCOLOR, activebackground=__BUTTONBGCOLOR_AC, activeforeground=__BUTTONFGCOLOR_AC, font=__BUTTONFONT)
        againButton.place(x=49, y=95, width=81, height=36)
        # background on entering widget
        againButton.bind("<Enter>", func=lambda e: againButton.config(
        background=__BUTTONBGCOLOR_AC, cursor="hand2"))
        # background color on leving widget
        againButton.bind("<Leave>", func=lambda e: againButton.config(
        background=__BUTTONBGCOLOR, cursor="hand2"))


def main():
    u = App()
if __name__ == "__main__":
    main()