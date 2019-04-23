# _*_ coding:utf-8 _*_

print('由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。')

def now():
	print('2018-10-31')
	
f1=now
print(f1)
print(f1.__name__)
print(f1())


print('\n 在函数调用前后自动打印日志，但又不希望修改now()函数的定义')

def log(fun):
	def wrapper(*args, **kw):
		print("call %s"%fun.__name__)
		return fun(*args, **kw)
	return wrapper
	
@log
def now2(x):
	print('now2:%d'%x)
	
now2(10)

print('\n 自定义log的文本。 有个小bug 它们的__name__已经从原来的\'now\'变成了\'wrapper\'')

def log2(text):
	def decorator(fun):
		def wrapper(*args, **kw):
			print("%s %s()"%(text, fun.__name__))
			return fun(*args,**kw)
		return wrapper
	return decorator
	
@log2('Excute')
def now3():
	print('now3 doing')

now3()

print(now3.__name__)


print('\n 自定义log的文本。 完美解决方案')

import functools
import sys

def log4(fun):
	@functools.wraps(fun)
	def wrapper(*args,**kw):
		print("call %s"%fun.__name__)
		return fun(*args, **kw)
	return wrapper
	
@log4
def now4():
	print('now4')
	
now4()
print(now4.__name__)


def log5(text):
	def decorator(fun):
		@functools.wraps(fun)
		def wrapper(*args,**kw):
			print('%s %s'%(text, fun.__name__))
			return fun(*args, **kw)
		return wrapper
	return decorator
	
@log5('Excute ')	
def now5():
	print('%s'%sys._getframe().f_code.co_name)
	
now5()
print(now5.__name__)


print('\n 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：')
import time
def log6(fun):
	@functools.wraps(fun)
	def wrapper(*args,**kw):
		print("call %s %s"%(fun.__name__, time.asctime(time.localtime(time.time()))))
		return fun(*args,**kw)
	return wrapper
	
@log6
def nowTime():
	print(' nowTime ing')
	
nowTime()



print('请编写一个decorator，能在函数调用的前后打印出\'begin call\'和\'end call\'的日志。')

def log7(*text):
	def decorator(fun):
		@functools.wraps(fun)
		def wrapper(*args,**kw):
			st = 'call'
			if len(text) > 0:
				st = text				
			print('%s begin call'%st)	
			re = fun(*args, **kw)	
			print('end call')				
			return re 		
		return wrapper		
	return decorator
	
def log72(fun):
	@functools.wraps(fun)
	def wrapper(*args,**kw):
		print('%s begin call'%'call')
		return fun(*args, **kw)
	return wrapper
	
	
@log7()
def now7():
	print('now7')
	return 'return now7'
	
print(now7())
		


	
