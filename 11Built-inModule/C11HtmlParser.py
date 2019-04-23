#_*_coding=utf-8_*_=
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print('<%s>' % tag, attrs)
		
	def handle_endtag(self,tag):
		print('</%s>'%tag)
		
	def handle_startendtag(self, tag, attrs):
		print('<%s/>'%tag)
		
	def handle_data(self, data):
		print(data)
		
	def handle_comment(self, data):
		print('<!--', data, '-->')
		
	def handle_entityref(self, name):
		print('&%s:'%name)
		
	def handle_charref(self, name):
		print('&#%s:'%name)
		
parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<pp/>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

print('''找一个网页，例如https://www.python.org/events/python-events/，
用浏览器查看源码并复制，然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。''')
from datetime import datetime
from urllib import request
import pdb
import sys
import copy

def myPrint(*args, **kw):
	pass
	
def print2(*args, **kw):
	pass

allPrint = myPrint

class MyHTMLParserEx(HTMLParser):


	def __init__(self):
		super(MyHTMLParserEx, self).__init__()
		self.titleBeg=False
		self.localBeg=False
		self.index=0
		self.perItem={}
		self.LiItem=[]

	
	def handle_starttag(self, tag, attrs):
		#pdb.set_trace()
		if tag == 'h3':
			for per in attrs:
				if len(per) == 2 and per[0] =='class' and per[1] == 'event-title':
					self.titleBeg=True
					
		if tag == 'time':
			for per in attrs:
				if len(per) == 2 and per[0] == 'datetime':
					print2(per[1])
					self.perItem['datetime'] = datetime.strptime(per[1], '%Y-%m-%dT%H:%M:%S+00:00')
					
		if tag == 'span':
			for per in attrs:
				if len(per) == 2 and per[0] == 'class' and per[1] == 'event-location':
					self.localBeg=True
					
		allPrint('<%s>' %tag, 'attrs=%s'%attrs)
		
	def handle_endtag(self, tag):
		allPrint('</%s>'%tag)
		
	def handle_startendtag(self, tag, attrs):
		allPrint('<%s>' %tag, 'attrs=%s'%attrs)
		
	def handle_data(self, data):
		if self.titleBeg == True and len(data) > 0:
			self.index = copy.copy(self.index + 1)
			self.perItem['index']= self.index
			self.perItem['title']= data
			self.titleBeg = False
			
		if self.localBeg == True and len(data) > 0:
			self.perItem['local']=data
			self.localBeg = False
			self.LiItem.append(copy.deepcopy(self.perItem))
			
		allPrint(data)
		
	def handle_comment(self, data):
		allPrint('<!--', data, '-->')
		
	def handle_entityref(self, name):
		allPrint('&%s:'%name)
		
	def handle_charref(self, name):
		allPrint('&#%s:'%name)

parser = MyHTMLParserEx()

with request.urlopen('https://www.python.org/events/python-events/') as f:
	#pdb.set_trace()
	parser.feed(f.read().decode('utf-8'))
	
for p in parser.LiItem:
	print(p)
	

