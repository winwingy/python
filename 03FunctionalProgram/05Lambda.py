# _*_ coding:utf-8 _*_
from functools import reduce
print('有些时候，不需要显式地定义函数，直接传入匿名函数更方便。')

li = map(lambda x:x*10, [1, 2, 3])
print(list(li))

li2 = reduce(lambda x,y : x*y, [1, 2, 3, 4])
print(li2)

print('也可以把匿名函数作为返回值返回')

def compute(a, b):
	return lambda : a*b
	
li3 = compute(10, 20)
print(li3)
print(li3())

def compute2():
	return lambda a,b: a*b
	
li4 = compute2()
print(li4)
print(li4(5, 4))


print('\nfilter(is_odd, range(1, 20))改造')

ret5=filter(lambda x:x%2==1, range(1, 20))
print(list(ret5))