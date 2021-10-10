import socket

PORT = 12345

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creating a socket object
    print("[+]SOCKET SUCCESSFULLY CREATED[+]")
except socket.error as err:
    print("[-]SOCKET CREATION FAILED WITH ERROR %s" %(err))

try:
    s.bind(('', PORT)) #Binds the socket '' is used to listen to any request from other computers on the network
    print("[+]SOCKET SUCCESSFULLY BOUND TO PORT %s" %(PORT))
except socket.error as err:
    print("[-]SOCKET CREATION FAILED WITH ERROR %s" % (err))

try:
    s.listen()#sets socket in listening mode
    print("[+]SOCKET IS LISTENING")
    while True:
        conn, addr = s.accept()#established a connection with client
        print("[+]CONNECTION ESTABLISHED:", addr)
        data = conn.recv(1024)#data is what ever the client sent over
        print(data)
        conn.send("[+]CONNECTION HAS BEEN ESTABLISHED".encode())#sends a message back
        conn.close()#closes connection
        break
except socket.error as err:
    print("[-]SOCKET CREATION FAILED WITH ERROR %s" % (err))