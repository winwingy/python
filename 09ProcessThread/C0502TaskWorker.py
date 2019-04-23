#_*_coding=utf-8_*_
import random,time,queue
from multiprocessing.managers import BaseManager

task_queue=queue.Queue()
result_queue=queue.Queue()

class QueueManager(BaseManager):
	pass
	

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr='127.0.0.1'
print('Connnect to server %s ...'%server_addr)

manager=QueueManager(address=(server_addr, 5000), authkey=b'abc')
manager.connect()
task=manager.get_task_queue()
result=manager.get_result_queue()

for i in range(10):
	try:
		n=task.get(timeout=1)
		print('run task %d*%d..'%(n,n))
		r='%d*%d=%d'%(n,n,n*n)
		time.sleep(1)
		result.put(r)
	except Queue.Empty:
		print('task queue is empty.')
		
print('worker exit.')
