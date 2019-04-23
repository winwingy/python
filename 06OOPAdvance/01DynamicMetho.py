#_*_coding=utf-8_*_

print('给实例绑定一个方法')
class Student(object):
	def printMy(self):
		print('student')
		
from types import MethodType
s = Student()

def set_age(self, age):
	self.age=age
	
s.set_age=MethodType(set_age, s)
s.set_age(10)
print(s.age)

print('对别一个实例是不起作用的')
s2 = Student()
#s2.set_age(1)


print('增加类的方法')
def set_score(self, score):
	self.score = score	
		
Student.set_score = set_score

s3=Student()
s3.set_score(5)
print(s3.score)


print('使用__slots__来限制该class实例能添加的属性')

class Animal(object):
	__slots__=('name','age')
	def printMy(self):
		print('Animal')
		
a=Animal()
a.name = 'jim'
a.age=10
#增加没有的属性不再成功
#a.score=100