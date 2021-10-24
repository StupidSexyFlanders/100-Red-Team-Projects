import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

FORMAT = 'UTF-8'
IP_ADDRESS = "192.168.1.73"
PORT = 12345

server.bind((IP_ADDRESS, PORT))


def client_thread(conn, addr):
    conn.send("Successful Connection to server".encode(FORMAT))
    print(str(addr) + " connected to server!")
    received = conn.recv(4096).decode(FORMAT)
    filename, data = received.split(',')
    file = open(filename, "w")
    file.write(data)
    file.close()
    print("File has been created")
    server.close()


def start():
    server.listen(50)
    print("SEVER STARTED")
    conn, addr = server.accept()
    print(addr[0] + " Connected")
    newClientThread = threading.Thread(target=client_thread, args=(conn, addr))
    newClientThread.start()


start()



