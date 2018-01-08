import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "0.0.0.0"
port = 800
file = open("text.txt", 'w')

try:
    server.bind((ip, port))#Escuta com um ip em uma determinada porta
    server.listen(5)#5 conexoes consecutivas
    print("Listening in..." + ip + "\n" + "Port: " + str(port)  )
    (client_socket, adress) = server.accept()
    print "Received from... " + adress[0]
    data = client_socket.recv(1024)
    if data == "0x56\n":
        client_socket.send("Welcome 0x/0x/0x/0x\n")
        while(True):
            response = client_socket.recv(1024)
            print(response)
            client_socket.send("ACK\n")
            file.write(response)
    else:
        client_socket.send("n0p!")
        server.close()
        exit()
except Exception as ex:
    print("Error:  " + str(ex))
    server.close()
