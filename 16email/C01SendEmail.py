#_*_coding=utf-8_*_=

'''
print('\n easy send email')
from email.mime.text import MIMEText
msg=MIMEText('hello, send by Python...', 'plain', 'utf-8')
from_addr='winwingy@qq.com'
password='ujumdqoictuwcbab'#input(from_addr + 'Passwor:')
smtp_server='smtp.qq.com'

to_addr='winwingy@163.com'

import smtplib
server=smtplib.SMTP()
server.set_debuglevel(1)
server.connect(smtp_server)
server.login(from_addr,password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
'''

'''
print('\n 发送一个完整的邮件')
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
	name, addr=parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))
	
from_addr='winwingy@qq.com'
password='ujumdqoictuwcbab'#input(from_addr + 'Passwor:')
smtp_server='smtp.qq.com'

to_addr='winwingy@163.com'

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From']=_format_addr('Python爱好者 <%s>'%from_addr)
msg['To']=_format_addr('管阿 <%s>'%to_addr)
msg['Subject']=Header('来自SMTP的问题。。', 'utf-8').encode()

server=smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
'''

'''
print('\n 发送HTML邮件')
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
	name, addr=parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))
	
from_addr='winwingy@qq.com'
password='ujumdqoictuwcbab'#input(from_addr + 'Passwor:')
smtp_server='smtp.qq.com'

to_addr='winwingy@163.com'

msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
msg['From']=_format_addr('Python爱好者 <%s>'%from_addr)
msg['To']=_format_addr('管阿 <%s>'%to_addr)
msg['Subject']=Header('来自SMTP的问题。。', 'utf-8').encode()

server=smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
'''

'''
print('\n 发送附件')
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart,MIMEBase
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
	name, addr=parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))
	
from_addr='winwingy@qq.com'
password='ujumdqoictuwcbab'#input(from_addr + 'Passwor:') ‘nctwyjwalgiibjaa’ nctwyjwalgiibjaa
smtp_server='smtp.qq.com'

to_addr='iceyeer@qq.com'

msg=MIMEMultipart()
msg['From']=_format_addr('黑猫警长 <%s>'%from_addr)
msg['To']=_format_addr('爱猫的冰叶 <%s>'%to_addr)
msg['Subject']=Header('喵喵喵', 'utf-8').encode()

msg.attach(MIMEText('<html><body><h1>'
'<a href="https://mp.weixin.qq.com/s/SghmRUC20TD474R1DbAMTA">看我家的小喵</a></h1>'
'<p align="center"><font color="#0000FF" size="5">send by wingy</font></p></body></html>', 'html', 'utf-8'))
	
# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('E:/0test/猫.jpg', 'rb') as f:
	mime=MIMEBase('image', 'png', filename='猫.jpg')
	mime.add_header('Content-Disposition', 'attachment', filename='猫.jpg')
	mime.add_header('Content-ID', '<0>')
	mime.add_header('X-Attachment-Id', '0')
	mime.set_payload(f.read())
	encoders.encode_base64(mime)
	msg.attach(mime)

server=smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

'''


'''
print('\n 发送嵌图片的邮件')
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart,MIMEBase
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
	name, addr=parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))
	
from_addr='winwingy@qq.com'
password='ujumdqoictuwcbab'#input(from_addr + 'Passwor:')
smtp_server='smtp.qq.com'

to_addr='winwingy@163.com'

msg=MIMEMultipart()
msg['From']=_format_addr('黑猫警长 <%s>'%from_addr)
msg['To']=_format_addr('爱猫的冰叶 <%s>'%to_addr)
msg['Subject']=Header('喵喵喵', 'utf-8').encode()

msg.attach(MIMEText('<html><body><h1>Hello</h1>'
'<p><img src="cid:0"</p></body></html>', 'html', 'utf-8'))
	
# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('E:/0test/猫.jpg', 'rb') as f:
	mime=MIMEBase('image', 'png', filename='猫.jpg')
	mime.add_header('Content-Disposition', 'attachment', filename='猫.jpg')
	mime.add_header('Content-ID', '<0>')
	mime.add_header('X-Attachment-Id', '0')
	mime.set_payload(f.read())
	encoders.encode_base64(mime)
	msg.attach(mime)

server=smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
'''




print('\n 发送加密邮件')
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart,MIMEBase
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
	name, addr=parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))
	
from_addr='winwingy@qq.com'
password='ujumdqoictuwcbab'#input(from_addr + 'Passwor:')
smtp_server='smtp.qq.com'

to_addr='winwingy@163.com'

msg=MIMEMultipart()
msg['From']=_format_addr('黑猫警长 <%s>'%from_addr)
msg['To']=_format_addr('爱猫的冰叶 <%s>'%to_addr)
msg['Subject']=Header('喵喵喵', 'utf-8').encode()

msg.attach(MIMEText('<html><body><h1>Hello</h1>'
'<p></p></body></html>', 'html', 'utf-8'))

server=smtplib.SMTP(smtp_server, 587)
server.set_debuglevel(1)
server.starttls()
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
