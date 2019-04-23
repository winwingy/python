# _*_ coding=utf-8 _*_

print(type(123))
print(type('abc'))

class Animal(object):
	def __init__(self):
		self.__name = 'a'
		self.age = 1
	
	
	def printMy(self):
		print('I am Animal')
		
	
		
a=Animal()
print(type(a))

print('要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：')
import types
def run():
	print('run')
	
print(type(run))

print(types.FunctionType)
print(type(run) == types.FunctionType)
print(type(abs))
print(type(lambda x:x))
print(types.LambdaType)


print('并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：')

print(isinstance(123, (str, int)))
print(isinstance('a', (str, int)))


print('如果要获得一个对象的所有属性和方法，可以使用dir()函数')

print(dir('abc'))


print('测试该对象的属性')
class Cat(Animal):
	def printMy(self):
		print('Cat')

c = Cat()		
print(hasattr(c, 'age'))
print(hasattr(Cat, 'age'))# false 类没有属性的， 只有对象有

print(getattr(c, 'age', 2))
print(getattr(c, 'hometown', 3))

print(hasattr(Cat, 'printMy'))#类有方法， 没有属性
print(getattr(Cat, 'printMy'))#类有方法， 没有属性



print('让一个类支持len')
class BigCat(Cat):
	def __len__(self):
		return 10
		
b =BigCat()
print(len(b))


print('可以直接在class中定义属性，这种属性是类属性，归Student类所有：')
class Tiger(BigCat):
	color='yellow'
	
t = Tiger()
print(t.color)
print(Tiger.color)
t.color='red'
print(t.color)
del t.color
print(t.color)
del Tiger.color
print('删除属性后会报错')
#print(t.color)

print('为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：')
class Student(object):
	count = 0
	def __init__(self,name):
		Student.count = Student.count + 1
		self.__name = name
		
	def printMy(self):
		print(self.__name, Student.count)

stu = Student('tom')
stu.printMy()

stu2 = Student('Jim')
stu2.printMy()




