#_*_coding=utf-8_*_
import pdb
print('\n\n sys operate')
import os
print(os.name)
print(os.environ)

print('\npath', os.path)

print('os.environ.path: %s'%os.environ.get('PATH'))

print('\n\n 查看、创建和删除目录可以这么调用：')
print(os.path.abspath('.'))
d2 = os.path.join(os.path.abspath('.'), 'testdir')
os.mkdir(d2)
os.rmdir(d2)

print('\n\n 拆分路径：')
li2 = os.path.split(d2)
print(li2)

print('\n\n os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：：')
li3 = os.path.splitext(d2)
d3 = os.path.join(d2, 'abc.txt')
li4 = os.path.splitext(d3)
print(li3)
print(li4)

print('\n\n 文件操作使用下面的函数：')
#os.rename('abc.txt', 'abc1.txt')

print('\n\n 列出当前目录下的所有目录：')
li5 = [ x for x in os.listdir('.') if not os.path.isdir(x)]
print(li5)
li6=os.listdir('e:/')
print(li6)

print('\n\n 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径')

def hasStr(str, fi):
	return str.find(fi) != -1
	
def addDirFiles(li, str):
	fi = []
	lid=[]
	for x in li:
		if os.path.isdir(x):
			lid.append(x + '/') 
		elif hasStr(x, str):
			fi.append(x)
	return fi,lid
	
	
def listDir(di, str):
	chs=[]
	[chs.append(di + x) for x in os.listdir(di)]
	fi, lid = addDirFiles(chs, str)
	for d in lid:
		fiList = listDir(d, str)
		for y in fiList:
			fi.append(y)
		
	return fi
		
	
def listDirOut(di, str):
	ret = listDir(di,str)
	print(ret)
	li = []
	for x in ret:
		li.append(x.replace(di, './'))
	return li
	
ret = listDirOut('E:/0test/', '.txt')
print(ret)

