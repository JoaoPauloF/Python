import socket 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect(("127.0.0.1", 777))
    client.send("0x56\n")  
    pacotes_recebidos = client.recv(1024)
    print pacotes_recebidos
except Exception as ex :
    print "Unable to connect. "
    print ex




