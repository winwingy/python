#_*_coding=utf-8_*_=
import hashlib
md5=hashlib.md5()
md5.update(b'how to use md5 in')
md5.update(b'python hashlib?')
print(md5.hexdigest())

md2=hashlib.md5()
md2.update('how to use md5 in'.encode('utf-8'))
md2.update('python hashlib?'.encode('utf-8'))
print(md2.hexdigest())

print('\n sha1')
sha=hashlib.sha1()
sha.update(b'how to use sha1 in')
sha.update(b'python hashlib')
print(sha.hexdigest())


print('\n 根据修改后的MD5算法实现用户登录的验证：')
db={}

def get_md5(s):
	return hashlib.md5(s.encode('utf-8')).hexdigest()

def regitster(username, password):
	db[username]=get_md5(username+password+'salt')
	
def login(username, password):
	try:
		ps = db[username]
		if get_md5(username+password+'salt') == ps:
			print('login success')
		else:
			print('login fail')
	except BaseException as e:
		print(e, 'not regester')
		
userList=(('jim', '123'),('tom', '123'), ('lily', 'abc'))
for x in userList:
	regitster(x[0], x[1])
	
login('jim', '123')
login('jim', '4')
login('jim1', '123')