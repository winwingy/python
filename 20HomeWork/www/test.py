'''
#_*_coding=utf-8_*_=
'''
#_*_coding:utf-8_*_
print('你好')


class MyDict(dict):
	def __getattr__(self, key):
		return di.get(key)

di = dict()
di['name'] = 'lily'
print(di)
print(getattr(di, 'name', None))

li = [1, 2, 3]
li2 = [ x*10 for x in li]
print(li2)

'''
import orm
from models import User, Blog, Comment
import asyncio

@asyncio.coroutine
def test(loop):
	yield from orm.create_pool(loop, user='www-data', password='www-data', db='awesome')
	u = User(name='wingy2', email='wingy2@qq.com', passwd='1234567890', image='about:blank')
	
	yield from u.save()	
	ret = yield from User.findAll()
	for x in ret:
		print(x)

import time
def mysleep():
	for x in range(11):
		time.sleep(1)


	
import os
if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	print('before run')
	loop.run_until_complete(test(loop))
	print('after run')
	mysleep()
	loop.close()
	
'''

import inspect

def a(a, b=0, *c, d, e=1, **f):
	pass
	
aa = inspect.signature(a)
print("inspect.signature(fn) is : %s" % aa)
print("inspect.signature(fn) type is : %s " % type(aa))
print("\n")

bb = aa.parameters
print("signature.parameters is: %s " % bb)
print("signature.parameters type is: %s" % type(bb))

for cc, dd in bb.items():
	print("mappingproxy.items()返回的两个值分别是：%s 和 %s"%(cc, dd))
	print("mappingproxy.items()返回的两个值的类型分别是：%s 和  %s"%(type(cc), type(dd)))
	print("\n")
	ee = dd.kind
	print("Parameter.kind属性是:%s" % ee)
	print("Parameter.kind属性的类型是:%s" % type(ee))
	print("\n")
	gg = dd.default
	print("Parameter.default的值是: %s" % gg)
	print("Parameter.default的类型是：%s" % type(gg))
	print("\n")
	
ff = inspect.Parameter.KEYWORD_ONLY
print("inspect.Parameter.KEYWORD_ONLY的值是:%s" % ff)
print("inspect.Parameter.KEYWORD_ONLY的类型是:%s" % type(ff))
	






