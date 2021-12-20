import socket
import json
from tkinter.messagebox import NO



class clientSocket():
    __HEADER_SIZE = 64
    __PORT = 54321
    __HOST = None
    __FORMAT = 'utf-8'

    # triger command
    __LOGIN = "log in"
    __LOGOUT = "log out"
    __SIGNUP = "sign up"
    __TRACKING = "tracking"
    __DISCONNECTED = "quit"

    # status
    # connect
    CONNECTING = "connecting status"
    SERVEROFFLINE = "server offline"
    ERRORCONNECT = "error connection"
    DISCONNECTEDCONN = "disconnected"
    # log in
    LOGINSUCCESSFUL = "login successful"
    WRONGPASS = "wrong password"
    # sign up
    SIGNUPSUCCESSFULL = "sign up success"
    IDEXIST = "ID existed"
    # tracking

    def __init__(self):
        # declare socket
        self.__client = None
        self.__RESULTS = None

    def send(self, msg):
        __message = msg.encode(self.__FORMAT)
        __msg_length = len(__message)
        __send_length = str(__msg_length).encode(self.__FORMAT)
        __send_length += b' ' * (self.__HEADER_SIZE - len(__send_length))
        self.__client.send(__send_length)
        self.__client.send(__message)

    def receive(self):
        __header_msg = self.__client.recv(
            self.__HEADER_SIZE).decode(self.__FORMAT)
        if __header_msg:
            header_msg_length = int(__header_msg)
            msg = self.__client.recv(header_msg_length).decode(self.__FORMAT)
            return msg

    def sendRequest(self, request, attachment_1, attachment_2, attachment_3):
        try:
                # request bao gồm "log in" "log out" "sign up" "tracking"
            if self.receive() == "open":
                self.send(request)
                if request == self.__LOGIN:
                    self.send(attachment_1) #ID
                    self.send(attachment_2) #PASS
                    __result = self.receive()
                    if __result == self.LOGINSUCCESSFUL:
                        return self.LOGINSUCCESSFUL
                    elif __result == self.WRONGPASS:
                        return self.WRONGPASS
                if request == self.__SIGNUP:
                    # if (attachment_2 == attachment_3):
                    self.send(attachment_1) # ID
                    self.send(attachment_2) # PASS
                    __result = self.receive()
                    if __result == self.SIGNUPSUCCESSFULL:
                        return self.SIGNUPSUCCESSFULL
                    elif __result == self.IDEXIST:
                        return self.IDEXIST
                if request == self.__LOGOUT:
                    self.send(self.__LOGOUT)
                if request == self.__TRACKING:
                    self.send(attachment_1) #place
                    self.send(attachment_2) #date
                    self.__RESULTS = json.loads(self.receive())
                    return self.__RESULTS
                if request == self.__DISCONNECTED: # này nếu muốn thì tạo 1 nút ngắt kết nối với server
                    self.send(self.__DISCONNECTED)
                    self.__client.close()
                    return self.DISCONNECTEDCONN
            else:
                return self.SERVEROFFLINE
        except:
            return self.ERRORCONNECT

    def start(self, ip):
        self.__HOST = ip
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        __ADDRESS = (self.__HOST, self.__PORT)
        try:
            self.__client.settimeout(1)
            self.__client.connect(__ADDRESS)
            self.__client.settimeout(None)
            if self.receive() == "open":
                __RUN = True
                return self.CONNECTING
            else:
                self.__client.close()
                return self.ERRORCONNECT
        except:
            return self.ERRORCONNECT


