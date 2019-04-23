#_*_coding=utf-8_*_=
import sys
print(sys.version)
import chardet

data='离离原上草，一岁一枯荣'.encode('utf-8')
r = chardet.detect(data)
print(r)

data = '最新の主要ニュース'.encode('euc-jp')
r = chardet.detect(data)
print(r)