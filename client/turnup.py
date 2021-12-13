import os
import tkinter as tk
from tkinter import Button, ttk
from PIL import Image, ImageTk
from entry import *
from tkinter import messagebox
from UI import *
class turnup(tk.Frame):
    __HEIGHT = 360
    __WIDTH = 640
    __BGCOLOR = "#fcfafa"
    __BUTTONBGCOLOR = "#0b0d1a"
    __BUTTONFGCOLOR = "#cecfd1"
    __BUTTONBGCOLOR_AC = "#5c5e6b"
    __BUTTONFGCOLOR_AC = "#ffffff"
    __BUTTONFONT = "roboto 11 bold"
    __NAMEPAGECOLOR = "#494b59"
    __BGENTRY = "#fafafa"
    __FGENTRY = "#f5f5f5"
    __WRAPCOLOR = "#f0f0f0"
    __ERRORFLOATINGCOLOR = "#0b0d1a"
    data = {"value": None, "date": None}
    isLogOut = False
    isTurnUp = False
    isInTurnUpPage = False

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

        # user account
        __account = tk.Frame(__wrapper, bg = self.__WRAPCOLOR)
        __account.place(x = 20, y = 16, width=180, height=34)
        # avatar
        __avtImg = Image.open("./img/avatar.png")
        __avatar = ImageTk.PhotoImage(__avtImg)
        __labelAvatar = tk.Label(__account, image=__avatar, bg = self.__WRAPCOLOR)
        __labelAvatar.image = __avatar
        __labelAvatar.place(x=0, y=0)
        
        self.__labelUsername = tk.Label(__account, text="hcmusMMT2012", bg = self.__WRAPCOLOR, fg=self.__NAMEPAGECOLOR, font = "roboto 13 normal")
        self.__labelUsername.place(x=40, y=6)

        # log out
        __logoutButton = tk.Button(__wrapper, text = "Log Out", 
            bg=self.__BUTTONBGCOLOR, fg=self.__BUTTONFGCOLOR, 
            activebackground=self.__BUTTONBGCOLOR_AC, activeforeground=self.__BUTTONFGCOLOR_AC, 
            font=self.__BUTTONFONT)
        __logoutButton.place(x=198, y=16, width=72, height=36)
        # background on entering widget
        __logoutButton.bind("<Enter>", func=lambda e: __logoutButton.config(
            background=self.__BUTTONBGCOLOR_AC, foreground=self.__BUTTONFGCOLOR_AC, 
            cursor="hand2"))
        # background color on leving widget
        __logoutButton.bind("<Leave>", func=lambda e: __logoutButton.config(
            background=self.__BUTTONBGCOLOR, foreground=self.__BUTTONFGCOLOR, 
            cursor="hand2"))
        # log out clicked
        __logoutButton.bind("<Button-1>", func=lambda e: self.toLogOut())
        # name page
        __labelName = tk.Label(__wrapper, text="TURN UP", 
        bg = self.__WRAPCOLOR, fg=self.__NAMEPAGECOLOR, font = "roboto 20 normal")
        __labelName.place(x=94, y=54)

        # query input
        self.__queryInput = EntryWithPlaceholder(__wrapper, "Search...", "#7d7f8e")
        self.__queryInput.place(x=23, y=92, width=96, height=30)
        # date input
        self.__dateInput = EntryWithPickerDay(__wrapper,color="#7d7f8e")
        self.__dateInput.place(x=130, y=92, width=96, height=30)
        # search
        __iconSearch = tk.PhotoImage(file="./img/search.png")
        __searchButton = tk.Button(__wrapper, image=__iconSearch, 
            bg=self.__BUTTONBGCOLOR, activebackground=self.__BUTTONBGCOLOR_AC, 
            font=self.__BUTTONFONT)
        __searchButton.place(x=236, y=90, width=36, height=36)
        # background on entering widget
        __searchButton.bind("<Enter>", 
            func=lambda e: __searchButton.config(
                image=__iconSearch, 
                background=self.__BUTTONBGCOLOR_AC, 
                cursor="hand2"
            ))
        # background color on leving widget
        __searchButton.bind("<Leave>", func=lambda e: __searchButton.config(
                image=__iconSearch, 
                background=self.__BUTTONBGCOLOR, 
                cursor="hand2"
            ))
        # read and send data to search
        __searchButton.bind("<Button-1>", func=lambda e: self.readAndSend())

        # resultwrapper
        __resultWrapp = tk.Frame(__wrapper, bg = self.__WRAPCOLOR)
        __resultWrapp.place(x = 14, y = 139, width=274, height=171)
        # define column
        columns = ('No','Result', 'Date', 'Cases_Today')
        self.__treeClients = ttk.Treeview(__resultWrapp, columns=columns, show='headings')
        # define headings
        self.__treeClients.heading('No', text='No')
        self.__treeClients.heading('Result', text='Result')
        self.__treeClients.heading('Date', text='Date')
        self.__treeClients.heading('Cases_Today', text='Cases')
        self.__treeClients.grid(row=0, column=0, sticky='nsew')
        # define column size
        self.__treeClients.column('No', width=27, anchor=tk.CENTER)
        self.__treeClients.column('Result', width=80, anchor=tk.CENTER)
        self.__treeClients.column('Date', width=72, anchor=tk.CENTER)
        self.__treeClients.column('Cases_Today', width=69, anchor=tk.CENTER)
        # scrollbar
        __scrollbar = ttk.Scrollbar(__resultWrapp, orient=tk.VERTICAL, command=self.__treeClients.yview)
        self.__treeClients.configure(yscroll=__scrollbar.set)
        __scrollbar.grid(row=0, column=1, sticky='ns')
        __resultWrapp.rowconfigure(0, weight=1)
        # serial
        self.serial = 0

    def createItemTree(self, result, date, cases):
        self.serial = self.serial + 1
        __item = (self.serial, result, date, cases)
        self.__treeClients.insert('', tk.END, values=__item)
    
    def deleteItemTree(self):
        self.serial = 0
        for clientItem in self.__treeClients.get_children():
            self.__treeClients.delete(clientItem)

    def readAndSend(self):
        if (self.__queryInput.get() != "New Username") and (
            self.__dateInput.get() != "dd/mm/yyyy"):
            self.isTurnUp = True
            self.data["value"] = str(self.__queryInput.get())
            self.data["date"] = str(self.__dateInput.get())

    def toLogOut(self):
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
        __yesButton.bind("<Button-1>", func=lambda e: self.toBackLogIn(__warning))

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

    def toBackLogIn(self, windows):
        self.isLogOut = True
        windows.destroy()

    def changeACN(self, name):
        self.__labelUsername["text"] = name