import socket

ip = input("ip - ")
port = input("port - ")
porta = int(port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect ((ip, porta))
print("[+] connected")

while True:
	command = input("shell> ").encode()
	s.sendall(command)
	print("[+] command sent")

	data = s.recv(4096)
	if not data:
		break
	else:
		print(data.decode("utf-8"))

	print("code is over")
	s.close()



	

