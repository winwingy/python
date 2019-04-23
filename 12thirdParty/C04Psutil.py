#_*_coding=utf-8_*_=

import psutil
print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))

print(psutil.cpu_times())

for x in range(2):
	print(psutil.cpu_percent(interval=1, percpu=True))
	
print('\n 获取内存信息')
print(psutil.virtual_memory())

print(psutil.swap_memory())

print('\n 获取磁盘信息')

print(psutil.disk_partitions())
print(psutil.disk_usage('/'))
print(psutil.disk_usage('C:'))
print(psutil.disk_io_counters())

print('\n 获取网络信息')
print(psutil.net_io_counters())
print(psutil.net_if_addrs())
print('\n  获取网络接口状态')
print(psutil.net_if_stats())
#print('\n 获取当前网络连接信息')
#print(psutil.net_connections())

print('\n 获取进程信息')
print(psutil.pids())
p=psutil.Process(7032)
print(p.name())
print(p.exe())
print(p.cwd())
print(p.cmdline())
print(p.ppid())
print(p.parent())
print(p.children())
print(p.status())
print(p.username())
print(p.create_time())
#print('进程终端', p.terminal())
print(p.cpu_times())
print(p.memory_info())
print(p.open_files())
print(p.connections())
print(p.num_threads())
print(p.threads())
print(p.environ())
#结束进程
p.terminate()

print(psutil.test())