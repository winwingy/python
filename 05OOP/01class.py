# _*_ coding=utf-8 _*_

class Student(object):
	def __init__(self, name, age):
		self.name=name
		self.age=age
		
	def printMy(self):
		print(self.name, self.age)
		
stu = Student('jin', 18)
stu.printMy()


print('private变量')

class Student2(object):
	def __init__(self, name, age):
		self.__name = name
		self.__age = age
		
	def getName(self):
		return self.__name
		
	def getAge(self):
		return self.__age
		
	def setName(self, name):
		self.__name=name
		
	def printMy(self):
		print(self.__name, self.__age)
		
stu2=Student2('Tom', 1)
stu2.printMy()
stu2.setName('lily')
stu2.city='gaozhou'
stu2.printMy()
print(stu2.city)

print('内部的__name变量已经被Python解释器自动改成了_Student__name')
stu2.__name='fly'
print(stu2._Student2__name)
print(stu2.__name)


print('继承和多态')
class Animal(object):
	def run(self):
		print('animal running')
		
	def printMy(self, a):
		print(a.run())
		
class Cat(Animal):
	def run(self):
		print('Cat running quickly')
		
	def eat(self):
		print('Cat eat meat')
		
class BigCat(Cat):
	def run(self):
		print('BigCat running flyying')
		
		
a=Animal()
c=Cat()
bc=BigCat()
print(isinstance(a, Animal))
print(isinstance(bc, Animal))	
print(isinstance(bc, Cat))
print(isinstance(a, Cat))
a.printMy(a)
a.printMy(bc)
