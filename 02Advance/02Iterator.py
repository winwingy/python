# _*_ coding:utf-8 _*_
from collections import Iterable
for d in 'abcde':
	print(d)
	
for d in list(range(10)):
	print(d)
	
	
kk = {'name':'lili','age':15,'city':'gaozhou'}
for d in kk:
	print(d)
	
for val in kk.values():
	print(val)
	
for key,val in kk.items():
	print(key,val)

print('如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：')

print(isinstance('abc', Iterable))
print(isinstance((1, 2,3), Iterable))
print(isinstance(123, Iterable))


print('Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：')

for i,val in enumerate(list(range(5, 10))):
	print(i, val)
	
for i,val in enumerate(list(range(5, 20, 4))):
	print(i, val)
	
	
print('请使用迭代查找一个list中最小和最大值，并返回一个tuple：')
li = [5, 6, 1, 10, 2]

def getMaxMin(li):
	maxVal = li[0]
	minVal = li[0]
	for x in li:
		if x > maxVal:
			maxVal = x
		if x < minVal:
			minVal = x
	return maxVal, minVal
	
print(getMaxMin(li))
	