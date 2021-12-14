import socket
import threading
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

    # status
    __CONNEXISTED = "open"
    __CONNDEAD = "close"
    __INLOGIN = "in Log In"
    __INSIGNUP = "in Sign Up"
    __INTURNUP = "in Turn Up"
    __INCONNECT = "in Connect"
    def __init__(self):
        # declare UI obj
        self.ui = UI.App()
        # declare socket
        self.__client = None

    def send(self, msg): 
        __message = msg.encode(self.__FORMAT)
        __msg_length = len(__message)
        __send_length = str(__msg_length).encode(self.__FORMAT)
        __send_length += b' ' * (self.__HEADER_SIZE - len(__send_length))
        self.__client.send(__send_length)
        self.__client.send(__message)
        print(__message)

    def receive(self):
        __header_msg = self.__client.recv(self.__HEADER_SIZE).decode(self.__FORMAT)
        if __header_msg:
            header_msg_length = int(__header_msg)
            msg = self.__client.recv(header_msg_length).decode(self.__FORMAT)
            print(msg)
            return msg

    def run(self):
        # while the UI object is existing, a socket object will be inited, ran and 
        # closed until the UI object is dead
        __isUIExist = True
        while __isUIExist:
            # init socket client TCP
            self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            __isBEGIN = True
            while __isBEGIN:
                __isRUN = False
                # waiting to get data from entry IP address and try to connect
                # server if not connected, the error page will be displayed....
                try:
                    self.ui.showUpPage(connect)
                    self.ui.layerFrames[connect].isInConnectPage = True
                    self.__HOST = self.ui.layerFrames[connect].data["ip"]
                    if self.__HOST:
                        self.ui.layerFrames[connect].data["ip"] = None #reset a ip variable
                        ADDRESS = (self.__HOST, self.__PORT)
                        self.__client.connect(ADDRESS)
                        __isRUN = True
                        # check if the connection exists after it is accepted by the server
                        if self.receive() != self.__CONNEXISTED:
                            __isRUN = False
                            if not self.ui.layerFrames[connect].isError:
                                self.ui.layerFrames[connect].showErrConnection()     
                except:
                    if not self.ui.layerFrames[connect].isError:
                        self.ui.layerFrames[connect].showErrConnection()
                    pass
                # if connected, login page will be displayed. 
                # And the communication is done.
                if __isRUN:
                    self.ui.showUpPage(login)
                    self.ui.layerFrames[connect].isInConnectPage = False
                    self.ui.layerFrames[login].isInLogInPage = True
                    __STATUS = self.socket_client()
                    if __STATUS == 1:
                        __isBEGIN = False
                        # self.__client.close()
            __isUIExist = self.ui.winfo_exists()

    # a function to perform the communication function
    # between the client and the server
    def socket_client(self):
        try:
            __isRUN = True
            while __isRUN:
                print("da chay")
                # if self.receive() == self.__CONNEXISTED:
                    # log in
                if self.ui.layerFrames[login].isInLogInPage:
                    # self.send(self.__INLOGIN) ### SEND ###
                    if self.ui.layerFrames[login].isQuit:
                        print("davo")
                        __isRUN = False
                        if self.receive() == self.__CONNEXISTED:
                            self.send(self.__DISCONNECTED) ### SEND Quit ###
                        # reset
                        self.ui.layerFrames[login].resetLogin()
                        # close socket
                        self.__client.close()
                        # swap status frame
                        self.ui.layerFrames[login].isInLogInPage = False
                        self.ui.layerFrames[connect].isInConnectPage = True
                        return 1
                    else:
                        if self.ui.layerFrames[login].isToSignUp:
                            self.ui.showUpPage(signup)
                            # reset
                            self.ui.layerFrames[login].isToSignUp = False # reset isToSignUp because of one-click one send
                            # swap status frame
                            self.ui.layerFrames[login].isInLogInPage = False
                            self.ui.layerFrames[signup].isInSignUpPage = True
                        else:
                            if self.ui.layerFrames[login].isLogin:
                                if self.receive() == self.__CONNEXISTED:
                                    self.send(self.__LOGIN) ### SEND Log in###
                                self.ui.layerFrames[login].isLogin = False # reset isLogin because of one-click one send
                                __ID = self.ui.layerFrames[login].data["username"]
                                __PASSWORD = self.ui.layerFrames[login].data["password"]
                                # reset
                                self.ui.layerFrames[login].data["username"] = None
                                self.ui.layerFrames[login].data["password"] = None

                                if __ID and __PASSWORD:
                                    self.send(__ID) ### SEND ###
                                    self.send(__PASSWORD) ### SEND ###
                                    __AccountName = __ID
                                    # reset
                                    __ID = None
                                    __PASSWORD = None

                                    __RESPOND = self.receive() #** RECV **#
                                    if __RESPOND == self.__LOGINSUCCESSFUL:
                                        self.ui.showUpPage(turnup)
                                        # reset login page
                                        self.ui.layerFrames[login].resetLogin()
                                        # swap status frame
                                        self.ui.layerFrames[login].isInLogInPage = False
                                        self.ui.layerFrames[turnup].isInTurnUpPage = True
                                    if __RESPOND == self.__WRONGID or __RESPOND == self.__WRONGPASS:
                                        if not self.ui.layerFrames[login].isError:
                                            self.ui.layerFrames[login].showWrongLogIn()

                # sign up
                if self.ui.layerFrames[signup].isInSignUpPage:
                    # self.send(self.__INSIGNUP) ### SEND ###
                    if self.ui.layerFrames[signup].isBackPage:
                        self.ui.showUpPage(login)
                        # reset
                        self.ui.layerFrames[signup].isBackPage = False
                        # swap status frame
                        self.ui.layerFrames[signup].isInSignUpPage = False
                        self.ui.layerFrames[login].isInLogInPage = True
                    else:
                        # not isBackPage
                        if self.ui.layerFrames[signup].isSignUp:
                            if self.receive() == self.__CONNEXISTED:
                                self.send(self.__SIGNUP) ### SEND Sign Up###
                            self.ui.layerFrames[signup].isSignUp = False # reset isSignUp because of one-click one send
                            __NEWID = self.ui.layerFrames[signup].data["new username"]
                            __NEWPASS = self.ui.layerFrames[signup].data["new password"]
                            # reset
                            self.ui.layerFrames[signup].data["new username"] = None
                            self.ui.layerFrames[signup].data["new password"] = None
                            if __NEWID != None and __NEWPASS != None:
                                self.send(__NEWID) ### SEND ###
                                self.send(__NEWPASS) ### SEND ###
                                # reset
                                __NEWID = None
                                __NEWPASS = None

                                __RESPOND = self.receive() #** RECV **#
                                if __RESPOND == self.__SIGNUPSUCCESSFULL:
                                    self.ui.showUpPage(login)
                                    # swap ui frame
                                    self.ui.layerFrames[signup].isInSignUpPage = False
                                    self.ui.layerFrames[login].isInLogInPage = True
                                elif __RESPOND == self.__IDEXISTED:
                                    if not self.ui.layerFrames[signup].isError:
                                        self.ui.layerFrames[signup].showErrorSignUP()

                # tracking (turn up)
                if self.ui.layerFrames[turnup].isInTurnUpPage:
                    # change account name 
                    if __AccountName:
                        self.ui.layerFrames[turnup].changeACN(__AccountName)
                    if self.ui.layerFrames[turnup].isLogOut:
                        self.ui.showUpPage(login)
                        # reset
                        self.ui.layerFrames[turnup].changeACN("hcmusMMT2012")
                        self.ui.layerFrames[turnup].isLogOut = False
                        # swawp status frame
                        self.ui.layerFrames[turnup].isInTurnUpPage = False
                        self.ui.layerFrames[login].isInLogInPage = True
                        return 2
                    else:
                        # not isLogOut
                        if self.ui.layerFrames[turnup].isTurnUp:
                            if self.receive() == self.__CONNEXISTED:
                                self.send(self.__TRACKING) ### SEND Tracking ###
                            self.ui.layerFrames[turnup].isTurnUp = False # reset isTurnUp because of one-click one send
                            __VALUE = self.ui.layerFrames[turnup].data["value"]
                            __DATE = self.ui.layerFrames[turnup].data["date"]
                            # reset
                            self.ui.layerFrames[turnup].data["value"] = None
                            self.ui.layerFrames[turnup].data["date"] = None

                            if __VALUE != None and __DATE != None:
                                self.send(__VALUE) ### SEND ###
                                self.send(__DATE) ### SEND ###
                                # reset
                                __VALUE = None
                                __DATE = None
                                __RESPOND = self.receive() #** RECV **#
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

                # else:
                #     if not self.ui.isError:
                #         self.ui.showError()
                #     self.__client.close()
                #     # reset all
                #     self.ui.layerFrames[connect].isInConnectPage = False
                #     self.ui.layerFrames[login].isInLogInPage = False
                #     self.ui.layerFrames[signup].isSignUpPage = False
                #     self.ui.layerFrames[turnup].isTurnUp = False
                #     __isRUN = False
                #     return 1
            if not __isRUN:
                if not self.ui.isError:
                    self.ui.showError()
                self.__client.close()
                # reset all
                self.ui.layerFrames[connect].isInConnectPage = False
                self.ui.layerFrames[login].isInLogInPage = False
                self.ui.layerFrames[signup].isSignUpPage = False
                self.ui.layerFrames[turnup].isTurnUp = False
                return 1

        except:
            if not self.ui.isError:
                self.ui.showError()
            self.__client.close()
            # reset all
            self.ui.layerFrames[connect].isInConnectPage = False
            self.ui.layerFrames[login].isInLogInPage = False
            self.ui.layerFrames[signup].isSignUpPage = False
            self.ui.layerFrames[turnup].isTurnUp = False
            return 1
           
def main():
    client = clientSoc()
    socThread = threading.Thread(target=client.run)
    socThread.daemon = True
    socThread.start()

    client.ui.run()

if __name__ == "__main__":
    main()