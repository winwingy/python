# encoding:utf-8
# python 2.7
import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()


# 使用标准函数来代替lambda函数，避免python2.7中，pickle无法序列化lambda的问题
def get_task_queue():
	global task_queue
	return task_queue


# 使用标准函数来代替lambda函数，避免python2.7中，pickle无法序列化lambda的问题
def get_result_queue():
	global result_queue
	return result_queue


def startManager(host, port, authkey):
	# 把两个Queue都注册到网络上，callable参数关联了Queue对象，注意回调函数不能使用括号
	BaseManager.register('get_task_queue', callable=get_task_queue)
	BaseManager.register('get_result_queue', callable=get_result_queue)
	# 设置host,绑定端口port，设置验证码为authkey
	manager = BaseManager(address=(host, port), authkey=authkey)
	# 启动manager服务器
	manager.start()
	return manager


def put_queue(manager):
	# 通过网络访问queueu
	task = manager.get_task_queue()
	for i in range(10):
		n = random.randint(0, 1000)
		print ('Put task %d' % n)
		task.put(n)
		time.sleep(0.5)

def get_queue(manager):
	result = manager.get_result_queue()
	for i in range(10):
		r = result.get(timeout=100)
		print('Result: %s'%r)

if __name__ == "__main__":
	host = b'127.0.0.1'
	port = 5000
	authkey = b'abc'
	# 启动manager服务器
	manager = startManager(host, port, authkey)
	# 给task队列添加数据
	put_queue(manager)
	
	get_queue(manager)
	# 关闭服务器
	manager.shutdown
	print('manager exit')
