#_*_coding=utf-8_*_=

# 函数也是入参
'''
def now():
	print("hello time")
	
f = now;
f()
'''



#log 函数 通过装饰器来实现
'''
def log(func):
	def wrapper(*args, **kw):
		print("call %s():" % func.__name__)
		return func(*args, **kw)
	return wrapper
	
@log
def now2():
	print("now time")

now2()

@log
def now3(aa):
	print("now time %s" % aa)

now3("my param")
'''


#装饰器 本身带参数
'''
def log2(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print("%s  %s():"  % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log2('execute')
def show2(ss2):
	print('%s show'%ss2)
	
show2('yiqing')  # 等价于  log2('execute')(show2)
'''


#更改 给装饰器 修饰的函数的 __name__ 属性
import functools

def log3(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print("%s %s():" % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator
	
@log3('show right name')
def show3():
	print('sh my ')
	
show3()




