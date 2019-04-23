#_*_coding=utf-8_*_

print('@property use')
class Student(object):
	@property
	def name(self):
		return self.__name
	
	@name.setter
	def name(self, name):
		if not isinstance(name, str):
			raise TypeError('not srt')
		else:
			self.__name=name
		
s = Student()
s.name='jim'
print(s.name)

try:
	s.name=123
except TypeError:
	print('TypeError')
	
	
print('还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：')
class MidStudent(object):	
	@property
	def score(self):
		return 10
	
m=MidStudent()
print(m.score)
try:
	m.score=100
except:
	print('raise except')
		

print('请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：')
class Screen(object):
	@property
	def width(self):
		return self.__width
	
	@width.setter
	def width(self, wid):
		self.__width=wid
		
	@property
	def resolution(self):
		return -1
		
s=Screen()
s.width=10
print(s.width)

print(s.resolution)
try:
	s.resolution=50
except:
	print('except')
	
	

