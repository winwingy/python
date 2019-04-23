#_*_coding=utf-8_*_=
import sys
print(sys.version)
print(sys.version_info)
print(sys.path)
import requests
import json


print('\n post')
login_data={'sent' : '自然语言处理是计算机科学领域与人工智能领域中的一个重要方向'}
print(type(login_data))

headerstr = {'Content-Type': 'application/json'}

r=requests.post('http://10.92.183.191:5000/TsService/DepTs', headers=headerstr, data=json.dumps(login_data))
print(r.status_code)
print(r.text)