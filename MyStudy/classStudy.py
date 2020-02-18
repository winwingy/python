#_*_coding=utf-8_*_=

class Student(object):
	def hello(self, text):
		print('my name is ', text)
		
stu = Student()
stu.hello('jim')
print(type(Student))
print(type(stu))


#使用type 来创建类

def fn(self, text):
	print('hello ', text)

Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
h.hello('tom')
print(type(Hello))
print(type(h))


### metaclass 元类 先定义metaclass，就可以创建类，最后创建实例。 ###
class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		print('ListMetaclass __new__:')
		for k, v in attrs.items():
			print(k, v)
			
		attrs['add']=lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs)
		
class MyList(list, metaclass=ListMetaclass):
	def show(self, text):
		pass
		
	text='list'
	
li = MyList()
li.append(1)
li.add(2)
print(li)


### 多重继承的 metaclass ####
class User(Model):
	id = IntegerField('id')
	name = StringField('username')
	email = StringField('email')
	password = StringField('password')


class Field(object):
	def __init__(self, name, column_type):
		self.name = name
	




