# -*- coding=utf-8 -*-

import sys
import os
import chardet

print(sys.getdefaultencoding())
reload(sys)
sys.setdefaultencoding('utf-8')


print(sys.getdefaultencoding())


ac='获得和设置系统默认编码'
print(chardet.detect(ac))

print(type(ac))

print("decode的作用是将其他编码的字符串转换成unicode编码，如str1.decode('gb2312')，表示将gb2312编码的字符串转换成unicode编码。".decode('utf8').encode('gb2312'))
acu = ac.decode('utf8')
print 'type(acu)' + str(type(acu))

print(acu.encode('gb2312'))


u2=u'直接将某种编码的str进行encode成另一种编码str'
print(type(u2))

print(u2)


print(u'打开gb2312文件，含有繁体字')
fp = open('test2.txt', 'r')
text = fp.read()
print(type(text))
print(text)
print(chardet.detect(text))

try:
	textu = text.decode('gb2312')
except UnicodeDecodeError as er:
	print 'UnicodeDecodeError' + str(er)

textu = text.decode('gbk')
print(type(textu))
print(textu)



s2 = ''

os.system('pause')