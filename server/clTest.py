import socket
from tkinter.constants import TRUE

HEADER_SIZE = 64
PORT = 54321
FORMAT = 'utf-8'
DISCONNECTED = "quit"
HOST = "127.0.0.1"
ADDRESS = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

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

send("sign up")
send("test")
send("2")
print(receive())

send("login")
send("test")
send("2")
print(receive())

while TRUE:
    msg = input()
    if msg == DISCONNECTED:  #    DISCONNECTED = "quit":
        print("client quit")
        send(msg)
        break
    send(msg)
    DATA1 = receive()
    print(f"Số ca nhiễm trong hôm nay tại {msg} là: {DATA1}")
    

""" send("TP. Hồ Chí Minh")
DATA = receive()
print(f"Số ca nhiễm trong hôm nay tại TP.Hồ Chí Minh là: {DATA}")
send(input())
DATA1 = receive()
print(f"Số ca nhiễm trong hôm nay tại TP.Hồ Chí Minh là: {DATA1}")
send(input()) """