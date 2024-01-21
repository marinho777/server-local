import socket
s=socket.socket()
ip="192.168.0.36".encode()
port=int(input("port - "))
s.connect((ip, port))
first=s.recv(1e024)
print(first)
s.send(input("message to send back - "))
