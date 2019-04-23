#_*_coding=utf-8_*_=

def log(fun):
	def wrapper(*args,**kw):
		print('call %s():'%fun.__name__)
		return fun(*args, **kw)
	return wrapper
	
	

@log
def study():
	print('study')
	
study()

print('\n 在函数前后打日志')
def logEx(fun):
	def wrapper(*args, **kw):
		print('Begin call %s()'%fun.__name__)
		runFun = fun(*args, **kw)
		print('End call %s()'%fun.__name__)
		return runFun
	return wrapper
	
@logEx
def studyEx():
	print('stduy harder')
	
studyEx()

print('\n 在函数前后打日志，且增加自己的文字log')
def logText(text):
	def outWrapper(fun):
		def wrapper(*args,**kw):
			print('Begin call %s()'%fun.__name__)
			print('%s'%text)
			runFun = fun(*args, **kw)
			print('End call %s()'%fun.__name__)
			return runFun
		return wrapper
	return outWrapper
	
@logText('log Info')
def studyText():
	print('studyText')
	
@logText('log good study')
def studyGood():
	print('studyGood')
	
studyText()
studyGood()



