#_*_coding=utf-8_*_
import base64
te='binar'
e = base64.b64encode(str.encode(te))
print(e)

e = base64.b64encode(bytes(te, encoding='utf8'))
print(e)
d = base64.b64decode(e)
print(d)

te=b'i\xb7\x1d\xfb\xef\xff'
e2=base64.b64encode(te)
print(e2)
e2=base64.urlsafe_b64encode(te)
print(e2)
te=base64.urlsafe_b64decode(e2)
print(te)


print('\n 请写一个能处理去掉=的base64解码函数：')
def safe_base64_encode(bStr):
	ben = base64.b64encode(bStr)
	en = str(ben, encoding='utf8')
	en = en.replace('=', '')
	return en
	
def safe_base64_decode(te):
	ad = 4 - len(te)%4
	te = te + '='*ad
	en = base64.b64decode(te)
	return en

en = safe_base64_encode(b'abc+/-=')
print(en)
print(safe_base64_decode(en))