import socket
import sys

IP_ADDRESS = "192.168.1.73"
PORT = 12345
FORMAT = 'UTF-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 2:
    print("Usage Instruction\n python3 client.py <filename>")
    exit()

filename = str(sys.argv[1])

try:
    server.connect((IP_ADDRESS, PORT))
    print("Successful connection to: %s" % IP_ADDRESS)
    while True:
        file = open(filename, "r")
        data = file.read()
        server.send(f"{filename}{','}{data}".encode(FORMAT))
        file.close()
except socket.error as err:
    print("Connection failed with error: %s" % err)

server.close()

