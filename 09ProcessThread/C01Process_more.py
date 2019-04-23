#_*_coding=utf-8_*_
from multiprocessing import Queue,Process
import subprocess

if __name__ == '__main__':
	print('nslookup www.python.org')
	r = subprocess.call(['nslookup', 'www.python.org'])
	print('Exit code:', r)
	
	
if __name__ == '__main__':
	print('\n 子进程还需要输入，则可以通过communicate()方法输入：')
	p=subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, err=p.communicate(b'set q=mx\npython.org\nexit\n')
	print(output.decode('ansi'))
	print('Exit code:', p.returncode)
	

import os, time, random

def write(q):
	print('Process to write: %s'%os.getpid())
	for value in ['A','B','C']:
		print('Put %s to queue...'%value)
		q.put(value)
		time.sleep(random.random())
		
def read(q):
	print('Process to read: %s'%os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue.'%value)


if __name__ == '__main__':
	print('\n 进程间通信：')
	q=Queue()
	pw=Process(target=write, args=(q,))
	pr=Process(target=read, args=(q,))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()