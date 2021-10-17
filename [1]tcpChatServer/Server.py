import socket
import json
import sys
import threading

#AF_INET is address domain, SOCK_STREAM means data or characters read in a continuous flow
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
FORMAT = 'UTF-8'

if len(sys.argv) != 3:
    print("Usage: script <IP ADDRESS> <PORT>")
    exit()

#Gets the first and second argument from cmd prompt and assigns it to IP_ADDRESS and PORT
IP_ADDRESS = str(sys.argv[1])
PORT = int(sys.argv[2])

#Binding IP_Address and port to server
server.bind((IP_ADDRESS, PORT))


list_of_clients = []


def clientThread(conn, addr,):
    conn.send("Welcome to the server".encode())
    while True:
        try:
            #recieves messages from clients
            message = conn.recv(2048)
            #json.loads() parses valid json string and converts it to a python dict
            decodedMsg = json.loads(message.decode(FORMAT))
            if decodedMsg:
                #print message and address of user who just sent message on terminal
                print("["+addr[0]+"]" + " " + str(decodedMsg))
                broadcastMessage(decodedMsg, conn)
                #print(type(decodedMsg))
            else:
                #Message may have no content if connection is broken, which we then remove the connection
                remove(conn)
        except:
            continue


def broadcastMessage(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                #formats the message
                messageFormating = message['name'] + ": " + message['msg']
                #json.dumps converts previously json.loads() object into a string for sending
                dataToSend = json.dumps(messageFormating).encode(FORMAT)
                #print(dataToSend)
                clients.send(dataToSend)
            except:
                clients.close()
                #if link broken remove client
                remove(clients)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

def start():
    # Sets server to listen for 100 connections
    server.listen(100)
    while True:
        # Accepts a connection request and stores conn (socket object) and addr which contains IP address of client
        conn, addr = server.accept()
        # maintains a list of clients for broadcasting
        list_of_clients.append(conn)
        print(addr[0] + " Connected")
        #when ever there is a new accept a thread is created to star the clientThread function
        newClientThread = threading.Thread(target=clientThread, args=(conn, addr))
        newClientThread.start()


print("[SERVER RUNNING]")
start()