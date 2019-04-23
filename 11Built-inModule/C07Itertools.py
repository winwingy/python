#_*_coding=utf-8_*_=
import itertools
natuals=itertools.count(1)
cnt=0
for n in natuals:
	print(n)
	cnt=cnt+1
	if cnt >= 10:
		break
		
cs=itertools.cycle('ABC')
cnt=0
for c in cs:
	print(c)
	cnt=cnt+1
	if cnt >= 10:
		break
		
cs=itertools.repeat('ABC', 10)
cnt=0
for c in cs:
	print(c)

print('\n takewhile()等函数根据条件判断来截取出一个有限的序列：')
nat=itertools.count(2, 2)
ns=itertools.takewhile(lambda x:x<=20, nat)
print(list(ns))

print('\n chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：')
li3=itertools.chain('abc','efg')
print(li3)
print(list(li3))

print('\n groupby()把迭代器中相邻的重复元素挑出来放在一起：')
gb=itertools.groupby('AAABBCCAAA')
print(gb)
#print(dict(gb))
for key,group in gb:
	print(key, list(group))
	
print('\n 求自然数前N个偶数的和')

def sum_my(n):
	iter = itertools.count(2, 2)
	sumC=0
	cnt=0
	while True:
		cnt = cnt + 1
		if cnt <= n:
			sumC = next(iter) + sumC
		else:
			break
	return sumC
#0  2  4  6  8  10
print(sum_my(5))
print(sum_my(10))
