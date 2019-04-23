#_*_coding=utf-8_*_

print('\n\n open file like C')
f=open('e:/0test/test.txt', 'r')
text=f.read()
print(text)
f.close()

print('\n\n try ... finally来实现安全')
try:
	f2=open('e:/0test/test.txt','r')
	t2=f2.read(3)
	print(t2)
except BaseException as e:
	print('BaseException: ',e)
finally:
	if 'f2' in dir():
		f2.close()

		
print('\n\n 打开GBK文件')

with open('e:/0test/GBK.txt', 'r',encoding='gbk', errors='ignore') as f3:
	t3 = f3.read()
	print(t3)
	

print('\n\n 写文件')

with open('e:/0test/utf8.txt', 'w', encoding='utf-8') as f4:
	f4.write('你是不是傻的啊')