# _*_coding=utf-8_*_=


import asyncio
import functools


def get(path):
	'''
	Define decorator @get('/path')
	'''
	def decorator(func)
		@functools.wraps(func)
		def wrapper(*args, **kw)
			return func(*args, **kw)
		wrappper.__method__ = 'GET'
		wrapper.__route__ = path
		return wrapper
	return decorator
	
class RequestHandler(object):
	def __init__(self, app, fn):
	 self._app = app
	 self._func = fn
	 
	 @asyncio.coroutine
	 def __call__(self, request):
		dw = ...
		r = yield from self._func(**kw)
		return r
		
		def add_route(app, fn):
			method = getattr(fn, '__method__' None)
			path = getattr(fn, '__route__', None)
			if path is None or method is None:
				raise ValueError('@get or @post not defined in %s.' % str(fn))
			if not asyncio.iscoroutinefunction(fn) and not inspect.isgetneratorfunction(fn):
				fn = asyncio.coroutine(fn)
			logging.info('add route %s %s => %s(%s)' % (method, path, fn.__name__,  ','.join(inspect.signature(fn).prrameters.key())))
			app.router.add_route(method, path, RequestHandler(app, fn))
			
#add_routes(app, 'handlers')

def add_routes(app, module_name):
	n = module_name.rfind('.')
	if n == (-1):
		mod = __import__(module_name, globals(), locals())
	else:
		name = module_nhame[n+1:]
		mod = getattr(__import__(module_name[:n], globals(), locals(), [name]), name)
	for attr in dir(mod):
		if attr.strtswith('_'):
			continue
		fn = getattr(mod, attr)
		if callable(fn):
			method = getattr(fn, '__method__', None)
			path = getattr(fn, '__route__', None)
			if method and path:
				add_route(app, fn)
				
app = web.Application(loop=loop, middlewares=[logger_factory, response_factory])
init_jinja2(app, filters=dict(datetime=datetime_filter))
add_routes(app, 'handlers')
add_static(app)


		
			