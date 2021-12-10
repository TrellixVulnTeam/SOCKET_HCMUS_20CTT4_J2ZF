import socket
from tkinter.constants import FALSE, TRUE

HEADER_SIZE = 64
PORT = 54321
FORMAT = 'utf-8'
DISCONNECTED = "quit"
""" HOST = "127.0.0.1"
ADDRESS = (HOST, PORT) """

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def send(msg): 
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER_SIZE - len(send_length))
    client.send(send_length)
    client.send(message)

def receive():
    header_msg = client.recv(HEADER_SIZE).decode(FORMAT)
    if header_msg:
        header_msg_length = int(header_msg)
        msg = client.recv(header_msg_length).decode(FORMAT)
        print(f"msg receive: {msg}")
        return msg

def enter_IP():
    while True:
        print("Enter host IP: ")
        HOST = input()
        ADDRESS = (HOST, PORT)
        print (f"Host IP: {HOST}")
        try:
            client.connect(ADDRESS)
            if receive() == "open":
                send("quit")
                return ADDRESS
            else:
                print("wrong host IP")
        except:
            print("no host IP")
        
def socket_client():
    try:
        RUN = TRUE
        while RUN:           
            print ("enter request: ")
            request = input() # request bao gồm "log in" "log out" "sign up" "tracking"
            if receive() == "open":
                send(request)
                if request == "log in":
                    print ("enter ID:")
                    ID = input()
                    print("enter PASSWORD:")
                    PASSWORD = input()
                    send(ID)
                    send(PASSWORD)
                    print(receive())
                if request == "sign up":
                    print ("enter ID:")
                    ID = input()
                    print("enter PASSWORD:")
                    PASSWORD = input()
                    print("confirm PASSWORD again:")
                    PASSWORD_CONFIRM = input()
                    if (PASSWORD == PASSWORD_CONFIRM):
                        send(ID)
                        send(PASSWORD)
                        print(receive())
                    else:
                        print("wrong PASSWORD") #khi nhập 2 password khác nhau
                        send("a")
                        send("1")
                        print(receive() + "cái này chỉ xuất hiện khi nhập pass lần 2 khác lần 1 khi đăng ký")
                        continue
                if request == "log out":
                    send("log out")
                    print(receive())
                if request == "tracking":
                    print ("enter place: ")
                    PLACE = input()
                    send(PLACE)
                    CASES = int(receive())
                    print (f"TODAY CASES: {CASES}")
                if request == "quit": # này nếu muốn thì tạo 1 nút ngắt kết nối với server
                    RUN = FALSE
                    send("quit")
                    return 1
            else:
                print("server offline")
    except:
        print("server crash")
        return 2

def start():
    BEGIN = TRUE
    while BEGIN:
        RUN = FALSE
        try:        
            print("input HOST IP: ")
            HOST = input()
            ADDRESS = (HOST, PORT)
            print(ADDRESS)
            client.connect(ADDRESS)
            if receive() == "open":
                RUN = TRUE
            else:
                print("server is offline")
        except:
            print("wrong HOST IP")
            pass
        if RUN == TRUE:
            STATUS = socket_client()
            if STATUS == 1:
                BEGIN = FALSE

start()