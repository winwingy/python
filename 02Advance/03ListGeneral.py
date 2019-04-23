# _*_ coding:utf-8 _*_
import os
print(list(range(1, 10, 2)))

li = [x for x in range(20,30)]
print(li)

li = [x*2 for x in range(20,30)]
print(li)

li = [x*2 for x in range(20,30) if x%2==0]
print(li)


print('还可以使用两层循环，可以生成全排列：')
li = [x+y for x in 'abc' for y in '123']
print(li)

print('列出当前目录下的所有文件和目录名，可以通过一行代码实现：')
files = [d for d in os.listdir('.')]
print(files)

print('列表生成式也可以使用两个变量来生成list：')
stu={'name':'lili', 'age':'15', 'city':'gaozhou'}
li=[x+'='+y for x,y in stu.items()]
print(li) 

print('如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：')
stu={'name':'lili', 'age':15, 'city':'gaozhou'}
li=[x+'='+y for x,y in stu.items() if isinstance(y, str)]
print(li) 
