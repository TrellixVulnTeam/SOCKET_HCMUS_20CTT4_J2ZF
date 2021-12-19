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
        print(__message)

    def receive(self):
        __header_msg = self.__client.recv(
            self.__HEADER_SIZE).decode(self.__FORMAT)
        if __header_msg:
            header_msg_length = int(__header_msg)
            msg = self.__client.recv(header_msg_length).decode(self.__FORMAT)
            print(msg)
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
                    print(__result)
                    if __result == self.LOGINSUCCESSFUL:
                        return self.LOGINSUCCESSFUL
                    elif __result == self.WRONGPASS:
                        return self.WRONGPASS
                if request == self.__SIGNUP:
                    # if (attachment_2 == attachment_3):
                    self.send(attachment_1) # ID
                    self.send(attachment_2) # PASS
                    __result = self.receive()
                    print(__result)
                    if __result == self.SIGNUPSUCCESSFULL:
                        return self.SIGNUPSUCCESSFULL
                    elif __result == self.IDEXIST:
                        return self.IDEXIST
                if request == self.__LOGOUT:
                    self.send(self.__LOGOUT)
                    print(self.receive())
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
                print("server offline")
                return self.SERVEROFFLINE
        except:
            print("server crash")
            return self.ERRORCONNECT

    def start(self, ip):
        self.__HOST = ip
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        __ADDRESS = (self.__HOST, self.__PORT)
        print(__ADDRESS)
        try:
            self.__client.settimeout(1)
            self.__client.connect(__ADDRESS)
            self.__client.settimeout(None)
            if self.receive() == "open":
                __RUN = True
                print("chay")
                return self.CONNECTING
            else:
                print("server is offline")
                self.__client.close()
                return self.SERVEROFFLINE
            
        except:
            print("wrong HOST IP")
            return self.ERRORCONNECT

    def CASES_results(self):
        return self.__RESULTS

   
""" test = clientSocket()
if test.start("192.168.242.1"):
    print("connect successful") """
# if (test.send_request("log in", "luat", "pro", " ")):
#     print("continue")
# if (test.send_request("tracking", "TP. Hồ Chí Minh", "17/12/2021", " ")):
#     print (f"Số ca hôm nay của TP. Hồ Chí Minh là: {test.CASES_return()}")

# if (test.send_request("quit", "luat", "pro", " ")):
#     print("quit")

# if test.start("127.0.0.1"):
#     print("connect successful")

# if (test.send_request("tracking", "Đà Nẵng", "17/12/2021", " ")):
#     print (f"Số ca hôm nay của Đà Nẵng là: {test.CASES_return()}")
