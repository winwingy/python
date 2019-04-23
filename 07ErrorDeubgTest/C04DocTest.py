#_*_coding=utf-8_*_

print('\n\n DocTest use')

class Dict(dict):
	'''
	
	Simple dict but also support x.y.
	
	>>> d1=Dict()
	>>> d1['x']=100
	>>> d1.x
	100
	
	>>> d2=Dict()
	>>> d2.y=200
	>>> d2['y']
	200
	
	>>> d3=Dict(a=1,b=2,c=3)
	>>> d3.e
	Traceback (most recent call last):
	...
	AttributeError: 'Dict' object has no attribute 'e'
	'''
	def __init__(self, **kw):
		super(Dict, self).__init__(**kw)
		
	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'"%key)
	
	def __setattr__(self,key,value):
		self[key]=value
		

	
	
print('\n\n homework 对函数fact(n)编写doctest并执行：')
def fact(n):
	'''
	
	>>> fact(2)
	2

	>>> fact(5)
	120
	
	>>> fact('5')
	Traceback (most recent call last):
	...
	TypeError: 'fact' no support no int
	
	>>> fact(0)
	Traceback (most recent call last):
	...
	OverflowError: value exceed
	
	>>> fact(-10)
	Traceback (most recent call last):
	...
	OverflowError: value exceed
	
	>>> fact(100)
	Traceback (most recent call last):
	...
	OverflowError: value exceed
	
	'''
	
	if not isinstance(n, int):
		raise TypeError(r"'fact' no support no int")
	if n <= 0 or n>=100:
		raise OverflowError('value exceed')
	if n == 1:
		return 1
	return n*fact(n-1)
	
	
import doctest
if __name__=='__main__':	
	doctest.testmod()



