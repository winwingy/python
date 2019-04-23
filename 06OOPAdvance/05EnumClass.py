#_*_coding=utf-8_*_

print('枚举类')
from enum import Enum,unique

@unique
class Weekly(Enum):
	Mon=1
	Tue=2
	Wed=3
	Thu=4
	Fri=5
	Sat=6
	Sun=7
	
print(Weekly.Tue) 
print(Weekly['Wed'])
print(Weekly(4))
for name,member in Weekly.__members__.items():
	print('name=%s member=%s value = %d'%(name,member, member.value))

	
	
print('把Student的gender属性改造为枚举类型，可以避免使用字符串：')

@unique
class Gender(Enum):
	Man=1
	Weman=2
	
class Student(object):
	def __init__(self,name,gender):
		self.__name = name
		self.__gender = gender
		
	def printMy(self):
		print(self.__name, "  ", self.__gender)
		
s = Student('lily', Gender.Man)
s.printMy()
		







		