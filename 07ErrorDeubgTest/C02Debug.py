#_*_coding=utf-8_*_

print('\n\n assert use')
import logging
logging.basicConfig(level=logging.INFO)
def foo(n):
	assert(isinstance(n, str) or isinstance(n, int))
	ret = int(n)
	print(ret)
	return ret
	
def foo2():
	try:
		foo('123')
		foo(1)
		foo(1.1)
	except AssertionError as e:
		logging.exception(e)
	finally:
		print('foo2 End')
		
foo2()


print('\n\n把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：')
logging.debug('logging.debug(')
logging.info('logging.info(')
logging.warning('logging.warning(')
logging.error('logging.error(')
logging.critical('logging.critical(')

logging.log(logging.ERROR, 'logging.log(logging.ERROR')


print('\n\n  第4种方式是启动Python的调试器pdb，让程序以单步方式运行，')
import pdb
a=1+2
b=a+10
pdb.set_trace()
c=a+b

