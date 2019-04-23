#_*_coding=utf-8_*_
import time,threading

def loop():
	print('thread %s is running...'%threading.current_thread().name)
	n = 0
	while n<5:
		n=n+1
		print('thread %s >>> %s' % (threading.current_thread().name, n))
		time.sleep(1)
	print('thread %s ended'%threading.current_thread().name)


if __name__=='__main__':
	print('\nthread %s is running...'%threading.current_thread().name)
	t=threading.Thread(target=loop, name='LoopThread')
	t.start()
	t.join()
	print('thread %s ended.'%threading.current_thread().name)


balance=0
def run_change(n):
	for i in range(10000000):
		global balance
		balance = balance + n
		balance = balance - n
	
	
if __name__=='__main__':
	print('\n 多线程更改一个变量的bug: balance != 0')
	t1=threading.Thread(target=run_change, args=(5,))
	t2=threading.Thread(target=run_change, args=(8,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print(balance)
	
lock=threading.Lock()
def run_change_lock(n):
	for i in range(10000000):
		try :
			lock.acquire()
			global balance
			balance = balance + n
			balance = balance - n
		finally:
			lock.release()
		
if __name__=='__main__':
	print('\n 多线程更改一个变量的解决： 加锁！')
	balance = 0
	t1=threading.Thread(target=run_change_lock, args=(5,))
	t2=threading.Thread(target=run_change_lock, args=(8,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print(balance)
