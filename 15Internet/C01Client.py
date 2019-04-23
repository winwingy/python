#_*_coding=utf-8_*_=
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(s.recv(1024).decode('utf-8'))

while True:
	text = input('请输入')
	s.send(bytes(text, 'utf-8'))
	print(s.recv(1024).decode('utf-8'))
	if text == 'exit':
		break
		
print('Connection close')
s.close()