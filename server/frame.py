import os
import tkinter as tk
from tkinter import Button, StringVar, ttk
from tkinter.constants import FALSE, RIGHT, TRUE
from PIL import Image, ImageTk


class wrapperInfo:
    def __init__(self, parent, ip, port, y_coor):
        self.__WRAPCOLOR = "#c5c7d7"
        self.__TEXTCOLOR = "#494b59"
        self.__CONNECTINGCOLOR = "#389341"
        self.__DISCONNECTEDCOLOR = "#da5b00"
        self.__ERRORCONNECTIONCOLOR = "#bb0000"
        self.__BUTTONBGCOLOR = "#b80000"
        self.__BUTTONFGCOLOR = "#cecfd1"
        self.__BUTTONBGCOLOR_AC = "#e00000"
        self.__BUTTONFGCOLOR_AC = "#ffffff"
        self.__BUTTONFONT = "roboto 11 bold"
        self.__CONNECTING = "Connecting.."
        self.__DISCONNECTED = "Disconnected"
        self.__ERRORCONNECTION = "Error !!!"

        #wrapperInfo
        self.__wrapperInfo = tk.Frame(parent, bg = self.__WRAPCOLOR)
        self.__wrapperInfo.place(x = 0, y = y_coor, width=404, height=40)
        # ip
        __ipAdrr = StringVar()
        __labelIP = tk.Label(self.__wrapperInfo, textvariable=__ipAdrr, bg = self.__WRAPCOLOR, fg = self.__TEXTCOLOR, font = "roboto 11 bold")
        __ipAdrr.set(ip)
        __labelIP.place(x=16, y=9)
        # port
        __portNo = StringVar()
        __labelPort = tk.Label(self.__wrapperInfo, textvariable=__portNo, bg = self.__WRAPCOLOR, fg = self.__TEXTCOLOR, font = "roboto 11 bold")
        __portNo.set(str(port))
        __labelPort.place(x=156, y=9)
    
    def showStatus(self, status):
        # status
        self.__statusConn = StringVar()
        if status == self.__CONNECTING:
            self.__labelstatus = tk.Label(self.__wrapperInfo, textvariable=self.__statusConn, bg = self.__WRAPCOLOR, fg = self.__CONNECTINGCOLOR, font = "roboto 11 bold")
            # close connection
            self.__closeCNButton = tk.Button(self.__wrapperInfo, text = "X", bg=self.__BUTTONBGCOLOR, fg=self.__BUTTONFGCOLOR, activebackground=self.__BUTTONBGCOLOR_AC, activeforeground=self.__BUTTONFGCOLOR_AC, font=self.__BUTTONFONT)
            self.__closeCNButton.place(x=350, y=2, width=48, height=36)
            # background on entering widget
            self.__closeCNButton.bind("<Enter>", func=lambda e: self.__closeCNButton.config(
            background=self.__BUTTONBGCOLOR_AC, cursor="hand2"))
            # background color on leving widget
            self.__closeCNButton.bind("<Leave>", func=lambda e: self.__closeCNButton.config(
            background=self.__BUTTONBGCOLOR, cursor="hand2"))
        if status == self.__DISCONNECTED:
            self.__labelstatus = tk.Label(self.__wrapperInfo, textvariable=self.__statusConn, bg = self.__WRAPCOLOR, fg = self.__DISCONNECTEDCOLOR, font = "roboto 11 bold")
        if status == self.__ERRORCONNECTION:
            self.__labelstatus = tk.Label(self.__wrapperInfo, textvariable=self.__statusConn, bg = self.__WRAPCOLOR, fg = self.__ERRORCONNECTIONCOLOR, font = "roboto 11 bold")
        self.__statusConn.set(status)
        self.__labelstatus.place(x=224, y=9)

    def updateStatus(self, status):
        if status == self.__DISCONNECTED:
            self.__statusConn.set(status)
            self.__labelstatus.config(textvariable=self.__statusConn, fg = self.__DISCONNECTEDCOLOR)
            self.__closeCNButton.place_forget()
        if status == self.__ERRORCONNECTION:
            self.__statusConn.set(status)
            self.__labelstatus.config(textvariable=self.__statusConn, fg = self.__ERRORCONNECTIONCOLOR)
            self.__closeCNButton.place_forget()
        if status == self.__CONNECTING:
            self.__statusConn.set(status)
            self.__labelstatus.config(textvariable=self.__statusConn, fg = self.__CONNECTINGCOLOR)
            self.__closeCNButton.place(x=350, y=2, width=48, height=36)

global __USR
__USR = []
__PADDING = 8
__INFOITEM = 40
__YSIZE = 0
__CONNECTING = "Connecting.."
__DISCONNECTED = "Disconnected"
__ERRORCONNECTION = "Error !!!"

def creatItemClient(parent, ip, port):
    check = FALSE
    for item in __USR:
        if item["ip"] == ip:
            check = TRUE
            break
    if not check:
        global __YSIZE 
        __item = {}
        usr = wrapperInfo(parent, ip, port, __YSIZE)
        usr.showStatus(__CONNECTING)
        __item["ip"] = ip
        __item[wrapperInfo] = usr
        __USR.append(__item)
        __YSIZE = __YSIZE + __PADDING + __INFOITEM
    else: 
        updateItemClient(ip, __CONNECTING)

def updateItemClient(ip, status):
    for item in __USR:
        if item["ip"] == ip:
            item[wrapperInfo].updateStatus(status)

class frame(tk.Frame):
    def __init__(self, root):
        __HEIGHT = 540
        __WIDTH = 960
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
        __CONNECTING = "Connecting.."
        __DISCONNECTED = "Disconnected"
        __ERRORCONNECTION = "Error !!!"
        tk.Frame.__init__(self, root)
        

        __style = ttk.Style()
        __style.configure('My.TFrame', background=__BGCOLOR)
        self = ttk.Frame(self, style='My.TFrame')
        self.place(height=__HEIGHT, width=__WIDTH, x = 0, y = 0)
        self.config()

        __bannerImg = Image.open("./img/serverBanner.png")
        __banner = ImageTk.PhotoImage(__bannerImg)
        __labelImg = tk.Label(self, image=__banner, bg = __BGCOLOR)
        __labelImg.image = __banner
        __labelImg.place(x=__WIDTH/2, y=0)

        # wrapper
        __wrapper = tk.Frame(self, bg = __WRAPCOLOR)
        __wrapper.place(x = 16, y = 16, width=464, height=460)
        
        # name page
        __labelName = tk.Label(__wrapper, text="Clients", bg = __WRAPCOLOR, fg = __NAMEPAGECOLOR, font = "roboto 18 bold")
        __labelName.place(x=190, y=15)
        
        # close
        __closeButton = tk.Button(self, text = "Close", bg=__BUTTONBGCOLOR, fg=__BUTTONFGCOLOR, activebackground=__BUTTONBGCOLOR_AC, activeforeground=__BUTTONFGCOLOR_AC, font=__BUTTONFONT)
        __closeButton.place(x=416, y=490, width=64, height=36)
        # background on entering widget
        __closeButton.bind("<Enter>", func=lambda e: __closeButton.config(
        background=__BUTTONBGCOLOR_AC, cursor="hand2"))
        # background color on leving widget
        __closeButton.bind("<Leave>", func=lambda e: __closeButton.config(
        background=__BUTTONBGCOLOR, cursor="hand2"))

        # show info connection
        __inforWrapp = tk.Frame(__wrapper, bg = __WRAPCOLOR)
        __inforWrapp.place(x = 14, y = 45, width=437, height=399)
        __canvasInfo=tk.Canvas(__inforWrapp, bg=__WRAPCOLOR, width=500, height=400, scrollregion=(0,0,700,700))
        __inforScroll = tk.Scrollbar(__inforWrapp, orient = 'vertical')
        __inforScroll.pack(side=tk.RIGHT, fill=tk.Y)
        __inforScroll.config(command=__canvasInfo.yview)
        __canvasInfo.config(width=437, height=399)
        __canvasInfo.config(yscrollcommand=__inforScroll.set)
        __canvasInfo.bind('<Configure>', on_configure)
        __canvasInfo.pack(expand=True,side=tk.LEFT,fill=tk.BOTH)
        # dict for info
        creatItemClient(__canvasInfo, "1.1.1.1", 64158)
        creatItemClient(__canvasInfo, "1.1.1.2", 64158)
        creatItemClient(__canvasInfo, "1.1.1.3", 64158)
        creatItemClient(__canvasInfo, "1.1.1.4", 64158)
        updateItemClient("1.1.1.4", __ERRORCONNECTION)
        creatItemClient(__canvasInfo, "1.1.1.5", 64158)
        creatItemClient(__canvasInfo, "1.1.1.6", 64158)
        creatItemClient(__canvasInfo, "1.1.1.7", 64158)
        creatItemClient(__canvasInfo, "1.1.1.8", 64158)
        creatItemClient(__canvasInfo, "1.1.1.9", 64158)
        creatItemClient(__canvasInfo, "1.1.1.10", 64158)
        creatItemClient(__canvasInfo, "1.1.1.11", 64158)

