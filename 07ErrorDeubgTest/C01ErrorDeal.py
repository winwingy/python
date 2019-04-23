#_*_coding=utf-8_*_


def foo(n):
	return 10/n
	
def fooOut(s):	
	print(foo(int(s)))
	

def mainRun():
	print('value str:')
	fooOut('10')
	fooOut('20')
	print('value list:')
	fooOut([1,2,3])
	
try:
	mainRun()
except ZeroDivisionError as e:
	print('except %s'%e)
except TypeError as e:
	print('except %s'%e)
finally:
	print('finally')
	
print('Python内置的logging模块可以非常容易地记录错误信息：')
import logging


def foo2(n):
	return 10/n
	
def fooOut2(s):	
	print(foo2(int(s)))
	

def mainRun2():
	print('value str:')
	fooOut2('10')
	fooOut2('20')
	print('value list:')
	fooOut2([1,2,3])
	
try:
	mainRun2()
except ZeroDivisionError as e:
	logging.exception(e)	
except TypeError as e:
	logging.exception(e)
finally:
	print('finally')
	
print('End')


print('\n\nhomework 根据异常信息进行分析，定位出错误源头，并修复：')
from functools import reduce
#原错误的函数
#def str2num(s):
#    return int(s)
#修复的函数
def str2num(s):
	try:
		return int(s)
	except BaseException as e:
		logging.exception(e)
		return 0

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
