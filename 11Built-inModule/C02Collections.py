#_*_coding=utf-8_*_
from collections import namedtuple
Point = namedtuple('Point1', ['x','y'])
p=Point(1,2)
print(p)
print(type(p))

Circle = namedtuple('Circleclass', ['x','y', 'r'])
c=Circle(5,3,2)
print(c)

print('\n deque 支持双向高效操作')
from collections import deque
q=deque(['a','b','c'])
q.append('d')
q.appendleft('1')
print(q)
q.popleft()
print(q)

print('\n defaultdict')
from collections import defaultdict
dd=defaultdict(lambda:'N/A')
dd['key1']=10
print(dd['key1'])
print(dd['key2'])

print('\n OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：')
from collections import OrderedDict
d=dict([('a',1),('c',3),('b',2)])
print(d)
od=OrderedDict([('a', 1), ('c',3), ('b',2)])
print(od)
od['1']=10
print(od)

print('\n OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：')

class LastUpdateOrderedDict(OrderedDict):
	def __init__(self, capacity):
		super(LastUpdateOrderedDict, self).__init__()
		self._capacity=capacity
		
	def __setitem__(self,key,value):
		containsKey = 1 if key in self else 0
		if len(self) - containsKey >= self._capacity:
			last = self.popitem(last=False)
			print('remove:', last)
		if containsKey:
			del self[key]
			print('set:', (key, value))
		else:
			print('add:',(key,value))
		OrderedDict.__setitem__(self,key,value)
		
la = LastUpdateOrderedDict(2)
la['a']=1
la['b']=2
la['c']=3
print(la)
la['d']=4
print(la)

print('\n ChainMap的设置')
from collections import ChainMap
ad={'color':'red', 'user':'guest'}
bd={'color':'green','userxxxx':'admin'}
cd={'colorxxx':'yellow','user':'wingy'}
dd={'col':'yes','u':'o'}
combined=ChainMap(dd, ad, bd)
print(combined['color'])

combined=ChainMap(dd, bd, cd)
print(combined['user'])


print('\n Counter是一个简单的计数器，例如，统计字符出现的个数：')
from collections import Counter
c = Counter()
for ch in 'programming':
	c[ch] = c[ch] + 1
	
print(c)




