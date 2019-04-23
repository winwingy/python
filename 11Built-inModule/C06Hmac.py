#_*_coding=utf-8_*_=
import hmac
message=b'Hello world!'
key=b'secret'
h=hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())

print('\n 根据修改后的MD5算法实现用户登录的验证：')
db={}

def get_md5(username, password, salt):
	return hmac.new((username + salt).encode('utf-8'),
	password.encode('utf-8'), digestmod='MD5').hexdigest()

def regitster(username, password):
	db[username]=get_md5(username, password, 'salt')
	
def login(username, password):
	try:
		ps = db[username]
		if get_md5(username, password, 'salt') == ps:
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