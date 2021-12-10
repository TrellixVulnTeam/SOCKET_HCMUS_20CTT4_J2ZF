import socket
import threading
from tkinter.constants import FALSE, TRUE
from tkinter.messagebox import NO
import UI
from connect import *
from login import *
from signup import *
from turnup import *

class clientSoc:
    #socket value
    __HEADER_SIZE = 64
    __FORMAT = 'utf-8'
    __PORT = 54321
    __HOST = None
    
    #trigger command
    __DISCONNECTED = "quit"
    __LOGIN = "log in" 
    __SIGNUP = "sign up" 
    __TRACKING = "tracking"
    __LOGOUT = "log out" 
    __IDEXISTED = "ID existed"
    __LOGINSUCCESSFUL = "login successful"
    __WRONGPASS = "wrong password"
    __WRONGID = "wrong id"
    __SIGNUPSUCCESSFULL = "sign up success"

    # data key
    __VALUEKEY = "Country"
    __DATEKEY = "Date"
    __TODAYCASESKEY = "TodayCases"
    def __init__(self):
        # declare UI obj
        self.ui = UI.App()
        # declare socket
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def send(self, msg): 
        __message = msg.encode(self.__FORMAT)
        __msg_length = len(__message)
        __send_length = str(__msg_length).encode(self.__FORMAT)
        __send_length += b' ' * (self.__HEADER_SIZE - len(__send_length))
        self.__client.send(__send_length)
        self.__client.send(__message)

    def receive(self):
        __header_msg = self.__client.recv(self.__HEADER_SIZE).decode(self.__FORMAT)
        if __header_msg:
            header_msg_length = int(__header_msg)
            msg = self.__client.recv(header_msg_length).decode(self.__FORMAT)
            return msg

    def enter_IP(self):
        while True:
            self.ui.showUpPage(connect)
            self.__HOST = self.ui.layerFrames[connect].data["ip"]
            ADDRESS = (self.__HOST, self.__PORT)
            try:
                self.__client.connect(ADDRESS)
                if self.receive() == "open":
                    self.send("quit")
                    return ADDRESS
                else:
                    self.ui.layerFrames[connect].showErrConnection()
            except:
                self.ui.layerFrames[connect].showErrConnection()
        
    def socket_client(self):
        try:
            __isRUN = TRUE
            while __isRUN:
                if self.receive() == "open":
                    # log in
                    if not self.ui.layerFrames[login].isQuit:
                        if not self.ui.layerFrames[login].isToSignUp:
                            if self.ui.layerFrames[login].isLogin:
                                self.send(self.__LOGIN)
                                __ID = self.ui.layerFrames[login].data["username"]
                                __PASSWORD = self.ui.layerFrames[login].data["password"]
                                if __ID and __PASSWORD:
                                    self.send(__ID)
                                    self.send(__PASSWORD)
                                    __RESPOND = self.receive()
                                    if __RESPOND == self.__LOGINSUCCESSFUL:
                                        self.ui.showUpPage(turnup)
                                    if __RESPOND == self.__WRONGID or __RESPOND == self.__WRONGPASS:
                                        self.ui.layerFrames[login].showWrongLogIn()
                        else:
                            self.ui.showUpPage(signup)
                    else:
                        __isRUN = FALSE
                        self.send(self.__DISCONNECTED)
                        self.ui.showUpPage(connect)
                        return 1

                    # sign up
                    if not self.ui.layerFrames[signup].isBackPage:
                        if self.ui.layerFrames[signup].isSignUp:
                            self.send(self.__SIGNUP)
                            __NEWID = self.ui.layerFrames[signup].data["new username"]
                            __NEWPASS = self.ui.layerFrames[signup].data["new password"]
                            if __NEWID != None and __NEWPASS != None:
                                self.send(__NEWID)
                                self.send(__NEWPASS)
                                __RESPOND = self.receive()
                                if __RESPOND == self.__SIGNUPSUCCESSFULL:
                                    self.ui.showUpPage(login)
                                elif __RESPOND == self.__IDEXISTED:
                                    self.ui.layerFrames[signup].showErrorSignUP()
                    else:
                        self.ui.showUpPage(login)

                    # tracking (turn up)
                    if not self.ui.layerFrames[turnup].isLogOut:
                        self.send(self.__TRACKING)
                        __VALUE = self.ui.layerFrames[turnup].data["value"]
                        __DATE = self.ui.layerFrames[turnup].data["date"]
                        if __VALUE != None and __DATE != None:
                            self.send(__VALUE)
                            self.send(__DATE)
                            __RESPOND = self.receive()
                            try:
                                self.ui.layerFrames[turnup].deleteItemTree()
                                __itemValue = None
                                __itemDate = None
                                __itemTodayCases = None
                                for item in __RESPOND:
                                    __itemDate = item[self.__DATEKEY]
                                    __itemValue = item[self.__VALUEKEY]
                                    __itemTodayCases = item[self.__TODAYCASESKEY]
                                    self.ui.layerFrames[turnup].createItemTree(__itemValue, __itemDate, __itemTodayCases)
                            except:
                                continue
                    else:
                        self.ui.showUpPage(login)
        except:
            self.ui.showError()
            return 2

    def run(self):
        __isBEGIN = TRUE
        while __isBEGIN:
            __isRUN = FALSE
            try:        
                self.ui.showUpPage(connect)
                self.__HOST = self.ui.layerFrames[connect].data["ip"]
                if self.__HOST:
                    ADDRESS = (self.__HOST, self.__PORT)
                    self.__client.connect(ADDRESS)
                    if self.receive() == "open":
                        __isRUN = TRUE
                    else:
                        self.ui.layerFrames[connect].showErrConnection()
            except:
                self.ui.layerFrames[connect].showErrConnection()
                pass
            if __isRUN == TRUE:
                self.ui.showUpPage(login)
                __STATUS = self.socket_client()
                if __STATUS == 1:
                    __isBEGIN = FALSE
                
def main():
    client = clientSoc()
    socThread = threading.Thread(target=client.run)
    socThread.daemon = True
    socThread.start()

    client.ui.run()

if __name__ == "__main__":
    main()