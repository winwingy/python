#_*_coding=utf-8_*_


print('定制print打印的函数')

class Student(object):
	def __init__(self,name):
		self.__name=name
		
	def __str__(self):
		return 'Student object name:%s'%self.__name
		
s=Student('jim')
print(s)


print('__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的')
class MidStudent(object):
	def __init__(self,name):
		self.__name=name
		
	def __str__(self):
		return 'Student object name:%s'%self.__name
		
	__repr__=__str__
	
m=MidStudent('lily')
m


print('__iter__ __next__')
class BigStudent(object):
	def __init__(self):
		self.a=[0, 1, 2, 3]
		self.i=0
		
	def __iter__(self):
		self.i=0
		return self
		
	def __next__(self):
		if self.i >= len(self.a):
			raise StopIteration()
		ret = self.a[self.i]
		self.i=self.i+1		
		return ret
		
b=BigStudent()

for i in b:
	print(i)
	
for i in b:
	print(i)
	
	
print('要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：')
class Animal(object):
	def __init__(self):
		self.li=[1,2,3,4]
		
	def __getitem__(self,i):
		return self.li[i]
		
a=Animal()
print(a[2])

print('__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断')
class Bird(Animal):
	def __getitem__(self,i):
		if isinstance(i, int):
			return self.li[i]
		elif isinstance(i, slice):
			start=i.start
			stop=i.stop
			if start is None:
				start=0
			if stop is None:
				stop=len(self.li)
			li = []
			for i in range(start, stop):
				li.append(self.li[i])
				
			return li				
			
b = Bird()
print(b[2])
print(b[0:3])
print(b[:2])
print(b[:])


print('Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性')

class Bus(object):
	def __getattr__(self, attr):
		if attr=='name':
			return 'lily'
		elif attr=='getAge':
			return lambda x:x*2
		else:
			raise AttributeError('no attri %s'%attr)

b = Bus()
print(b.name)
print(b.getAge(5))

try:
	print(b.score)
except:
	print('no attr')
	
	
print('__call__相当于c++的函数对象')

class Food(object):
	def __call__(self):
		print('call Food')
		
f = Food()
f()


print(callable(max))
print(callable(f))
print(callable(123))








		