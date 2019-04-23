#_*_coding=utf-8_*_=
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
	te = input('请输入')
	s.sendto(bytes(te, 'utf-8'), ('127.0.0.1', 7788))
	print(s.recv(1024).decode('utf-8'))
	if te=='exit':
		break
s.close()
