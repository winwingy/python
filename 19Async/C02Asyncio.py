#_*_coding=utf-8_*_=

import asyncio
'''
@asyncio.coroutine
def hello():
	print('hello world!')
	r = yield from asyncio.sleep(1)
	print('hello again!')
	
loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()
'''

'''
print('\n我们用Task封装两个coroutine试试：')
import threading
import asyncio
import time


@asyncio.coroutine
def hello():
	print('Hello world! (%s)' % threading.currentThread())
	yield from asyncio.sleep(1)
	print('Hello again! (%s)' % threading.currentThread())
	
loop2 = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop2.run_until_complete(asyncio.wait(tasks))
loop2.close()
'''

'''
print('\n 我们用asyncio的异步网络连接来获取sina、sohu和163的网站首页：')
import asyncio
import time

@asyncio.coroutine
def wget(host):
	print('wget %s ...'% host)
	connect = asyncio.open_connection(host, 80)
	reader, writer = yield from connect
	header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
	writer.write(header.encode('utf-8'))
	yield from writer.drain()
	while True:
		line = yield from reader.readline()
		if line == b'\r\n':
			break
		print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
		time.sleep(1)
	writer.close()
	
loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.baidu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
'''


print('\n homework ')
import asyncio
import time
import threading
@asyncio.coroutine
def mywork(x):
	for i in range(10):
		print(x, i, threading.currentThread())
		yield from asyncio.sleep(1)
		
loop = asyncio.get_event_loop()
tasks = [mywork('a'), mywork('b')]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()



