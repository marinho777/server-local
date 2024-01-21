import socket
s=socket.socket()
ip="127.0.0.1".encode()
port=int(input("port - "))
s.connect((ip, port))

first=s.recv(1024)
print(first)
s.send(input("message to send back - "))
