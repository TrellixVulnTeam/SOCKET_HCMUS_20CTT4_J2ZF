import socket
import sys

LOGIN = "LOGIN"
SIGNUP = "SIGNUP"
SEARCH = "SEARCH"
END = "end"
FORMAT = "utf8"
BUFFERSIZE = 1024
HOSTSERVER = "127.0.0.1"
PORTLISTEN = 65431

class serverSoc(object):
    def __init__(self):
        self.__AddressFamiliy = socket.AF_INET
        self.__SocketType = socket.SOCK_STREAM

    def createSock(self):
        try:
            self.__serverSock = socket.socket(self.__AddressFamiliy, self.__SocketType)
        except socket.error as __err:
            print ("Error creating socket: %s" % __err)
            sys.exit(1)
        