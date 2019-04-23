#_*_coding=utf-8_*_=
import sys
print(sys.version)
print(sys.version_info)
print(sys.path)
import requests


r=requests.get('http://www.guimp.com/')
print(r.status_code)
print(r.text)

r=requests.get('http://www.guimp.com/', params={'q':'python','cat':'1001'})
print(r.url)
print(r.text)
print(r.content)

r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print('\n直接显示返回的json')
print(r.json())



print('\n post')
from urllib import parse
email='winwingy@163.com' 
passwd='123456'
login_data=parse.urlencode([
('username', email),
('password', passwd),
('entry', 'mweribo'),
('client_id',''),
('savestate','1'),
('ec',''),
('pagerefer','https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

headStr = [('Origin','https://passport.weibo.cn'),
	('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'),
	('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fpad.weibo.cn%2F')]
	
headList = {}
for x in headStr:
	headList[x[0]] = x[1]

r=requests.post('https://passport.weibo.cn/sso/login', headers=headList, data=login_data.encode('utf-8'))
print(r.status_code)
print(r.text)