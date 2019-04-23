#_*_coding=utf-8_*_

print('\n\n string IO')
from io import StringIO
f=StringIO()
f.write('Hello ')
f.write('world')
print(f.getvalue())

f2=StringIO('abcde\nefg')
while True:
	t2=f2.readline()
	if t2=='':
		break
	print(t2)

print('\n\n BytesIO')
from io import BytesIO

f3=BytesIO()
f3.write('中文'.encode('utf-8'))
print(f3.getvalue())

f3.write(b'\nabcd')
print(f3.getvalue())