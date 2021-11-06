import socket
import select
import sys
import json

base_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
specialCharacters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '\\', ',', '|', ';', ':', '"', '<', '.', '>', '/', '?', '[', ']', "'", ',']


#Creates a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#checks if users have inputed IP address, port and name in commandline arguments
if len(sys.argv) != 5:
    print("Usage Instruction:\n python3 client.py <IP ADDRESS> <PORT> <NAME> <switch>")
    exit()

#Assigns the command line arguments in to the following variable
IP_ADDRESS = str(sys.argv[1])
PORT = int(sys.argv[2])
NAME = str(sys.argv[3])
switch = int(sys.argv[4])

if switch > 25:
    print("Switch cannot be more than 25")
    exit()

#encoding format
FORMAT = 'UTF-8'
#Establishes connection to specified IP address and port
try:
    server.connect((IP_ADDRESS, PORT))
    print('[+][+][+]Connected to Server[+][+][+]')
except socket.error as err:
    print('[-]Socket creation failed[-]')

#Function to encodes the message
def decoder(caeEnc):
    decoded_msg_array = []
    for i in caeEnc:
        if i == ' ':
            decoded_msg_array.append(' ')
        elif i in base_alphabet:
            i = (base_alphabet.index(i) - switch) % 26
            decoded_msg_array.append(base_alphabet[i])
        else:
            i in specialCharacters
            pass
    decoded_msg = ''.join(decoded_msg_array).replace('  ', '')
    return decoded_msg

#Function to decode message
def encoding(uncoded):
    coded_msg_array = []
    for i in uncoded:
        if i == ' ':
            coded_msg_array.append(' ')
        elif i in base_alphabet:
            i = (base_alphabet.index(i) + switch) % 26
            coded_msg_array.append(base_alphabet[i])
        else:
            i in specialCharacters
            pass
    coded_msg = ''.join(coded_msg_array).replace('  ', '')
    return coded_msg

while True:
    uncoded = []
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
            name = decodedMsg.split(" ", 1)[0]
            name = name.replace("\"", "")
            print(name)
            caeEnc = decodedMsg.split(" ", 1)[1]
            plain_msg = decoder(caeEnc)
            display_msg = name.capitalize() + ' ' + plain_msg.lower()
            print(display_msg)
        else:
            message = sys.stdin.readline()
            for i in message:
                i = i.upper()
                uncoded.append(i)
            encoded_msg = encoding(uncoded)
            data = {'msg': encoded_msg, 'name': NAME}
            dataToSend = json .dumps(data).encode(FORMAT)
            server.send(dataToSend)
            sys.stdout.write("<You>: ")
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()
