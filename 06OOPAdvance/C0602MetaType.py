#_*_coding=utf-8_*_

print('一般的定义方法')
from C0601TypeBase import Hello
h=Hello()
h.printMy()

print(type(Hello))
print(type(h))

print('用type来定义类')

def show(self):
	print('show')
	
def showName(self,name):
	print(name)

City = type('City', (object,), dict(showMy=show, showName=showName))
c=City()
print(type(City))
print(type(c))
c.showMy()
c.showName('gaozhou')

print('metaclass相当于类的创建模板')
class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add']=lambda self, value:self.append(value)
		return type.__new__(cls, name, bases, attrs)
		
class ListBase(object):
	def __init__(self):
		self.li = []
	
	def append(self, val):
		self.li.append(val)
		
	def __str__(self):
		return str(self.li)
	
class MyList(ListBase, metaclass=ListMetaclass):
	pass
	
	
l=MyList()
l.add('a')
print(l)
l.add('b')
print(l)

print('而普通的list没有add()方法：')
li2=ListBase()
#li2.add('k')
print(li2)