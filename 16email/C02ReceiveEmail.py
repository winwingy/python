#_*_coding=utf-8_*_=

'''
import poplib
from email.parser import Parser

email='winwingy@qq.com'
password='ujumdqoictuwcbab'
pop3_server='pop.qq.com'

#server=poplib.POP3(pop3_server)
#QQ邮箱用下面
server=poplib.POP3_SSL(pop3_server, port=995)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))

server.user(email)
server.pass_(password)

print('Message:%s.Size:%s'%server.stat())
#list()返回所有的邮件的编号 
resp, mails, octets=server.list()
print(mails)

index=len(mails)
resp, lines, octets=server.retr(index)

msg_context=b'\r\n'.join(lines).decode('utf-8')
msg=Parser().parsestr(msg_context)

# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)
server.quit()
'''

from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import poplib

print('\n 解析邮件')

import sys
class LoggerMy(object):
	def __init__(self, filename="Default.log"):
		self.terminal = sys.stdout
		self.log = open(filename, "a")

	def write(self, message):
		self.terminal.write(message)
		self.log.write(message)

	def flush(self):
		pass

sys.stdout = LoggerMy("yourlogfilename.txt")
print("Hello world LoggerMy !") # this is should be saved in yourlogfilename.txt


def decode_str(s):
	value, charset=decode_header(s)[0]
	if charset:
		value=value.decode(charset)
	return value
	
def guess_charset(msg):
	charset=msg.get_charset()
	if charset is None:
		content_type=msg.get('Content-Type', '').lower()
		pos =content_type.find('charset=')
		if pos >= 0:
			charset = content_type[pos +8:].strip()
	return charset

def print_info(msg, indent=0):
	if indent == 0:
		for header in ['From', 'To', 'Subject']:
			value=msg.get(header, '')
			if value:
				if header=='Subject':
					value=decode_str(value)
				else:
					hdr, addr=parseaddr(value)
					name=decode_str(hdr)
					value=u'%s <%s>'%(name, addr)
			print('%s%s: %s' %('  '*indent, header, value))
	if (msg.is_multipart()):
		parts=msg.get_payload()
		for n, part in enumerate(parts):
			print('%spart %s' % (' ' * indent, n))
			print('%s ---------'%(' ' * indent))
			print_info(part, indent + 1)
	else:
		content_type=msg.get_content_type()
		if content_type=='text/plain' or content_type=='text/html':
			content = msg.get_payload(decode=True)
			charset=guess_charset(msg)
			if charset:
				content=content.decode(charset)
			print('%sText: %s'%(' '*indent, content + '...'))
		else:
			print('%sAttachment: %s'%(' '*indent, content_type))
			


email='winwingy@qq.com'
password='ujumdqoictuwcbab'
pop3_server='pop.qq.com'

#server=poplib.POP3(pop3_server)
#QQ邮箱用下面
server=poplib.POP3_SSL(pop3_server, port=995)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))

server.user(email)
server.pass_(password)

print('Message:%s.Size:%s'%server.stat())
#list()返回所有的邮件的编号 
resp, mails, octets=server.list()
print('返回所有的邮件的编号: ', mails)

index=len(mails)
resp, lines, octets=server.retr(index)
print('index = ', index)

msg_context=b'\r\n'.join(lines).decode('utf-8')
msg=Parser().parsestr(msg_context)
print('递归地打印出Message对象的层次结构：')
print_info(msg)

		

# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)
server.quit()
