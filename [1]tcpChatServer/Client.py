import socket
import select
import sys
import json

#Creates a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#checks if users have inputed IP address, port and name in commandline arguments
if len(sys.argv) != 4:
    print("Usage Instruction:\n python3 client.py <IP ADDRESS> <PORT> <NAME>")
    exit()

#Assigns the command line arguments in to the following variable
IP_ADDRESS = str(sys.argv[1])
PORT = int(sys.argv[2])
NAME = str(sys.argv[3])

#encoding format
FORMAT = 'UTF-8'
#Establishes connection to specified IP address and port
server.connect((IP_ADDRESS, PORT))

while True:
    socket_list = [sys.stdin, server]

    """
    Two possible input situations, first is the manual input of user sending message,
    other is server sending message. Select later return from the socket_list which is 
    the stream reader for input. If loop handle messages sent from server, the else
    condition handles message sending from user
    """

    read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            decodedMsg = message.decode(FORMAT)
            decodedMsg = decodedMsg.replace("\\n", "")
            print(decodedMsg)
        else:
            message = sys.stdin.readline()
            data = {'msg': message, 'name': NAME}
            dataToSend = json .dumps(data).encode(FORMAT)
            server.send(dataToSend)
            sys.stdout.write("<You>: ")
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()