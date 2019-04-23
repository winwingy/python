#_*_coding=utf-8_*_=
print('\n 实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。')

class Query(object):
	def __init__(self, name):
		self.name = name
		
	def __enter__(self):
		print('Begin')
		return self
		
	def __exit__(self, exc_type, exc_value, traceback):
		if exc_type:
			print('Error')
		else:
			print('End')
			
	def query(self):
		print('Query info about %s..'%self.name)
		
with Query('bob') as q:
	q.query()
	
print('\n 编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法')
from contextlib import contextmanager

class Query(object):
	def __init__(self, name):
		self.name=name
	
	def query(self):
		print('Query info about %s ..'%self.name)
		
	def close(self):
		print('close')
		
@contextmanager
def create_query(name):
	print('Begin')
	q=Query(name)
	yield q
	q.close()
	print('End')
	
with create_query('tom') as q:
	q.query()
	
	
print('\n 我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现')
@contextmanager
def tag(name):
	print('begin %s'%name)
	yield
	print('end %s'%name)
	
with tag('lily'):
	print('do work!')

print('\n 如果一个对象没有实现上下文，我们就不能把它用于with语句。'
'这个时候，可以用closing()来把该对象变为上下文对象。'
'例如，用with语句使用urlopen()：')
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
	for line in page:
		print(line)

