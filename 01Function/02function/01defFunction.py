# _*_ coding:utf-8 _*_

def myMax(a,b):
	if a > b:
		return a
	return b
	
val = myMax(5, 6)
print(val)

def myAbs(a):
	pass
	
	
	
#检查函数，抛出异常

def myFullAbs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	return -x

val2 = myFullAbs('5')