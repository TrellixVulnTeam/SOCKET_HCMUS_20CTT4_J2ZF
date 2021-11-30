import socket
import threading
import UI
import crawl
from userData import *

class serverSoc:
    # socket value
    __HEADER_SIZE = 64
    __FORMAT = 'utf-8'
    __PORT = 54321
    __HOST = "127.0.0.1"
    __ADDRESS = (__HOST, __PORT)

    # store clients
    __CLIENTS = []

    # trigger command
    __LOGIN = "logIn"
    __SIGNUP = "signUp"
    __TURNUP = "turnUp"
    __CONNECT = "connect"
    __DISCONNECTED = "quit"

    # status
    __CONNECTINGSTATUS = "Connecting.."
    __DISCONNECTEDSTATUS = "Disconnected"
    __ERRORCONNECTIONSTATUS = "Error !!!"

    def __init__(self):
        # crawl data covid from "https://static.pipezero.com/covid/data.json"
        # declare crawl data obj
        self.crData = crawl.crawlDataCov()
        # declare UI obj
        self.ui = UI.App()
        # declare user data obj
        self.__userDB = userDB()

        # declare socket
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.__server.bind(self.__ADDRESS)
        self.__server.listen()
        # self.run()

    def receive(self, conn):
        try:
            header_msg = conn.recv(self.__HEADER_SIZE).decode(self.__FORMAT)
            if header_msg:
                header_msg_length = int(header_msg)
                msg = conn.recv(header_msg_length).decode(self.__FORMAT)
                return msg
        except:
            return None
    
    def send(self, conn, msg): 
            message = msg.encode(self.__FORMAT)
            msg_length = len(message)
            send_length = str(msg_length).encode(self.__FORMAT)
            send_length += b' ' * (self.__HEADER_SIZE - len(send_length))
            conn.send(send_length)
            conn.send(message)

    def run(self):
        while True:
            conn, addr = self.__server.accept() # conn is a pointer point to client if server connecting, addr is client's ip and port
            self.ui.creatItemClient(addr[0], addr[1])
            self.__CLIENTS.append(str(addr))
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.daemon = True
            thread.start()

        
    def handle_client(self, conn, addr):
        run = True
        if (self.access(conn, addr)):
            try:
                while run:
                    msg = self.receive(conn)
                    if msg == self.__DISCONNECTED:
                        self.__CLIENTS.remove(str(addr))
                        self.ui.creatItemClient(addr[0], addr[1], self.__DISCONNECTEDSTATUS)
                        print(msg)
                        run = False
                        break
                    data = str(self.crData.query(msg))
                    self.send(conn, data)
                conn.close()
            except SyntaxError:
                self.ui.creatItemClient(addr[0], addr[1], self.__ERRORCONNECTIONSTATUS)
                conn.close()
        else:
            conn.close()
    
    def access(self, conn, addr):
        run = True
        try:
            while run:
                REQUEST = self.receive(conn)
                if REQUEST == None:
                    self.__CLIENTS.remove(str(addr))
                    self.ui.creatItemClient(addr[0], addr[1], self.__ERRORCONNECTIONSTATUS)
                    return False
                if REQUEST == self.__DISCONNECTED:
                    self.__CLIENTS.remove(str(addr))
                    self.ui.creatItemClient(addr[0], addr[1], self.__DISCONNECTEDSTATUS)
                    return False
                if REQUEST == "sign up":

                    ID = self.receive(conn)
                    PASSWORD = self.receive(conn)
                    try:
                        self.__userDB.check(ID,PASSWORD)
                        self.send(conn, "ID existed")                    
                    except:
                        account = user(ID, PASSWORD)
                        self.__userDB.writeToLocal(account)
                        self.send(conn, "sign up success")                       
                    continue
                if REQUEST == "login":
                    try:
                        ID = self.receive(conn)
                        PASSWORD = self.receive(conn)
                        # print(user_data.query(ID)["password"])
                        if self.__userDB.check(ID, PASSWORD):
                            # print("login successful")
                            self.send(conn, "login successful")
                            return True
                        else:
                            # print("wrong password")
                            self.send(conn, "wrong password")
                    except:
                        # print("ID don't exist")
                        self.send(conn, "wrong id")                   
        except SyntaxError:
            # print("Error - disconnected")
            self.ui.creatItemClient(addr[0], addr[1], self.__ERRORCONNECTIONSTATUS)
            return False

def main():
    serv = serverSoc()
    crThread = threading.Thread(target=serv.crData.run)
    socThread = threading.Thread(target=serv.run)
    crThread.daemon = True
    socThread.daemon = True
    crThread.start()
    socThread.start()

    serv.ui.run()

if __name__ == "__main__":
    main()