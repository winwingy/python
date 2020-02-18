#_*_coding=utf-8_*_=

'''

#调试级的 wsgiref
from wsgiref.simple_server import make_server


def application(environ, start_response):
	#print(environ)	
	start_response('200 OK', [('Content-Type', 'text/html')])
	body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
	return [body.encode('utf-8')]

	
def handle_home(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	return b'<h1>hello home!</h1>'
	
def hadle_signin(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	path = environ['PATH_INFO'][1:]
	body = '<h1>Hello, signin %s!</h1>' % path
	return [body.encode('utf-8')]

def application2(environ, start_response):
	method = environ['REQUEST_METHOD']
	path = environ['PATH_INFO']
	if method == 'GET' and path == '/':
		return handle_home(environ, start_response)
	if method=='POST' and path=='/signin':
		return handle_signin(environ, start_response)
	else:
		start_response('200 OK', [('Content-Type', 'text/html')])
		path = environ['PATH_INFO'][1:]
		body = '<h1>Hello, %s!</h1>' % path
		return [body.encode('utf-8')]
	

httpd = make_server('', 8000, application2)
print('Serving HTTP on port 8000...')
httpd.serve_forever()

'''


"""
#应用级的 Flask
from flask import Flask

from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	return '<h1>Home</h1>'
	

@app.route('', methods=['get', 'post'])
def noPath():
	return '<h1>no path</h1>'

	
@app.route('/signin', methods=['GET'])
def signin_form():
	return '''<form action="/signin" method="post">
				<p><input name="username"></p>
				<p><input name="password" type="password"></p>
				<p><button type="submit">Sign In</button></p>
				</form>'''
				
@app.route('/signin', methods=['POST'])
def signin():
	#需要从request对象读取表单内容
	if request.form['username'] == 'admin' and request.form['password']=='password':
		return '<h3>Hello, admin!</h3>'	
	return '<h3>invalid user or password!</h3>'
		
if __name__ == '__main__':
	app.run()

"""

#用框架模板来实现
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('homeTest.html')
	
@app.route('/signin', methods=['GET'])
def sigin_form():
	return render_template('formTest.html')
	
@app.route('/signin', methods=['POST'])
def signin():
	username = request.form['username']
	password = request.form['password']
	if username=='admin' and password=='password':
		return render_template('signinTest-ok.html', username=username)
	return render_template('formTest.html', message='Bad userhname or password',  username=username)
	
if __name__ == '__main__':
	app.run()
		
	
	




	
