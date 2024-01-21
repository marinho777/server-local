import socket
s=socket.socket()
port = int(input("port - "))
s.bind(("127.0.0.1", port))
while True:
	print("[+] waiting for connection")
	s.listen(1)
	acc = s.accept()
	print("[+] received a connection")
	msg = input("input the message to send - ").encode()
	s.send(msg)
	ac1=s.recv(1024)
	print(ac1)
