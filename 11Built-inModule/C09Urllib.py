#_*_coding=utf-8_*_=
print('\n url get')
from urllib import request
'''
with request.urlopen('http://home.fdzh.org/') as f:
	data = f.read()
	print('Status:', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s:%s'%(k,v))
	print('Data:', data.decode('utf-8'))

print('\n 模拟手机请求网页')

req=request.Request('http://www.douban.com/')
req.add_header('User-Agent',  'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
	print('Status:', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s: %s'%(k, v))
	print('Data:', f.read().decode('utf-8'))
	
'''
print('\n post请求')
from urllib import parse
import json
email='winwingy@163.com' #input('Email:')
passwd='' #input('Password:')
login_data=parse.urlencode([
('username', email),
('password', passwd),
('entry', 'mweribo'),
('client_id',''),
('savestate','1'),
('ec',''),
('pagerefer','https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req=request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin','https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fpad.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
	print('Status:', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s : %s' % (k, v))
	bodyJs = f.read().decode('utf-8')
	print('Data:',bodyJs)
	body = json.loads(bodyJs)
	print(body['msg'])
	
	
print('\n 通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理')
proxy_handler = urllib.request.ProxyHandler({'http':'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener=urllib.request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
	pass



