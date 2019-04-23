#_*_coding=utf-8_*_=
from wsgiref.simple_server import make_server
from C03WSGI_hello import application, application2

httpd = make_server('', 8000, application2)
print('Serving HTTP on port 8000...')
httpd.serve_forever()