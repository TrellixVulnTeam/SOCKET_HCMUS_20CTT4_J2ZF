import tkinter as tk
from tkinter import Widget, ttk
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

def main():
    u = App()
if __name__ == "__main__":
    main()