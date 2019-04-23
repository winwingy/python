#_*_coding=utf-8_*_=

def comsumer():
	r = ''
	while True:
		n = yield r
		if not n:
			return 
		print('comsumer %s' % n)
		r = '200 ok'
		
def producer(c):
	c.send(None)
	n = 0
	while n < 5:
		n = n + 1
		print('producer %d'%n)
		r = c.send(n)
		print('producer %d code %s'%(n, r))
	c.close()
	
c = comsumer()
producer(c)