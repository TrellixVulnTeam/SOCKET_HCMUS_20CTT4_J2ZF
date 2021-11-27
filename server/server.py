import socket
import threading
from crawl import *
from userData import *
from tkinter import *
from PIL import ImageTk, Image
HEADER_SIZE = 64
FORMAT = 'utf-8'
DISCONNECTED = "quit"
window = Tk()
PORT = 54321
HOST = "127.0.0.1"
#socket.gethostbyname(socket.gethostname())
#print (HOST)
ADDRESS = (HOST, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

CLIENTS = []

def receive(conn):
    header_msg = conn.recv(HEADER_SIZE).decode(FORMAT)
    if header_msg:
        header_msg_length = int(header_msg)
        msg = conn.recv(header_msg_length).decode(FORMAT)
        print(f"msg receive: {msg}")
        return msg

def send(conn, msg): 
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER_SIZE - len(send_length))
    conn.send(send_length)
    conn.send(message)

def access(conn, addr):
    run = True
    try:
        while run:
            user_data = userDB()
            REQUEST = receive(conn)
            if REQUEST == DISCONNECTED:
                CLIENTS.remove(str(addr))
                return False
            if REQUEST == "sign up":
                ID = receive(conn)
                PASSWORD = receive(conn)
                try:
                    print(user_data.query(ID)["password"])
                    print("ID existed")
                    send(conn, "ID existed")                    
                except:
                    account = user(ID, PASSWORD)
                    user_data.writeToLocal(account)
                    send(conn, "sign up success")                       
                continue
            if REQUEST == "login":
                try:
                    ID = receive(conn)
                    PASSWORD = receive(conn)
                    print(user_data.query(ID)["password"])
                    if PASSWORD == user_data.query(ID)["password"]:
                        print("login successful")
                        send(conn, "login successful")
                        return True
                    else:
                        print("wrong password")
                        send(conn, "wrong password")
                except:
                    print("ID don't exist")
                    send(conn, "wrong id")                   
    except SyntaxError:
        print("Error - disconnected")
        return False

def handle_client(conn, addr):
    run = True
    if (access(conn, addr)):
        try:
            while run:
                msg = receive(conn)
                if msg == DISCONNECTED:
                    CLIENTS.remove(str(addr))
                    run = False
                    break
                print(f"[{addr}] {msg}")
                cov = crawlDataCov()
                data = cov.query(msg)['casesToday']
                print(data)
                data = str(data)
                send(conn, data)
            print(f"[{addr}] quit")
            conn.close()
        except SyntaxError:
            print("Error - disconnected")
            conn.close()
    else:
        conn.close()
    
def start():
    server.listen()
    print(f"Server is listening on {HOST}") #phải có f để nó xuất ra địa chỉ HOST
    """ GUI_server() """
    
    
    while True:
        conn, addr = server.accept() # conn là con trỏ trỏ đến client mà server connecting, addr là địa chỉ ip và port của client
        CLIENTS.append(str(addr))
        for CLIENT in CLIENTS:
            print (f"client đang kết nối: {CLIENT}")
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"client number - {threading.active_count() - 6}" )
        
def clients_update():
    l.config(text=str(random.random()))
    window.after(1000, clients_update)

def GUI_server():
    IP1 = "192.168.72.1"
    PORT1 = str(65231)
    IP2 = "192.168.72.1"
    PORT2 = str(65231)
    SPACE_ROW = 50
    STATUS = "connected"

    window.title("server")
    window.geometry("950x540")
    """ window.configure(bg='white')  """
    window.resizable(width = False, height = False)

    background = ImageTk.PhotoImage(Image.open("./img/background.png"))
    picture = Label(window, image=background)
    picture.place(x = 470, y = 0)
    box = ImageTk.PhotoImage(Image.open("./img/bg.png"))
    box = Label(window, image=box)
    box.place(x = 5, y = 80)

    LBL = Label(window, text = "ACTIVE CLIENT:", fg="black", font = ("Arial", 35))
    LBL.place(x = 0, y = 0)

    for CLIENT in CLIENTS:
        lb = Label(window, text = CLIENT, fg = "black", font = ("Arial", 15))
        lb.place(x = 10, y = 100 + CLIENTS.index(CLIENT)*SPACE_ROW)

    window.mainloop()

start()