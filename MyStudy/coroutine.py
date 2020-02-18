#_*_conding=utf-8_*_

#协程的使用，协程是一个线程，但可以异步处理问题。效率极高

def consumer():
	r = ''
	while True:
		n = yield r
		if not n:
			return
		print('[CONSUMER] Consuming %s ...' %n)
		r = 'consuming %d 200 OK'%n
		
def produce(c):
	c.send(None)
	n = 0
	while n < 5:
		n = n + 1
		print('[PRODUCER] Producing %s ...' % n)
		r = c.send(n)
		print('[PRODUCER] Consumer return: %s' % r)
	c.close()
	
c = consumer()
produce(c)