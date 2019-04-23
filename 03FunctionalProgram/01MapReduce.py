# _*_ coding:utf-8 _*_
from functools import reduce

print('map use')
def AddFun(x):
	return x + 10
	
li = map(AddFun, [1, 2, 3, 4, 5])
print(list(li))


print('reduce use')

def TowFun(x,y):
	return x+y
	
li = reduce(TowFun, ['a','b','c','d'])
print(li)


print('reduce and map use')

Digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

def charToInt(x):
	return Digits[x]
	
def linkInt(x, y):
	return x*10 + y

li3 = reduce(linkInt, map(charToInt, '12345'))
print(li3)


print('把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入')

def nomalizeName(x):
	it = iter(x)
	ret = next(it).upper()
	for i in it:
		ret = ret + i.lower()
		
	return ret

li4 = map(nomalizeName, ['jim', 'tOM', 'LILY'])
print(list(li4))
	
print('请编写一个prod()函数，可以接受一个list并利用reduce()求积：')
def prod(x, y):
	return x*y
	
li5 = reduce(prod, [1, 2, 3, 4, 5])
print(li5)


print('lambda use')

a=lambda x : x*2
print(a(5))

lamFun2=lambda x,y : x*y
print(lamFun2(5, 6))

