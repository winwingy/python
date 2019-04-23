#_*_coding=utf-8_*_
import re

reg=r'^\d{3,4}([-]|\s+)\d{6,8}$'
print(re.match(reg, '010   6688888'))
print(re.match(reg, '010-6688888'))
print(re.match(reg, 'u1010-6688888'))
print(re.match(reg, 'u1010-6688-888'))
print(re.match(reg, '1010-6688888-'))
print(re.match(reg, '1010-6688888'))


print('\n切分字符串')
print(re.split(r'\s+', 'a b   c 	 d'))
print(re.split(r'[\s\,]+', 'a , b   c 	 d'))
print(re.split(r'[\s\,;]+', 'a , b   ;;c 	 d'))

print('\n分组显示')
m = re.match(r'^(\d{3,4})(-|\s+)(\d{6,8})$', '010  6688888')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))

m2=re.match(r'^([0-9]{1,2})\:([0-9]{1,2})\:([0-9]{1,2})$', '11:55:00')
print(m2)
print(m2.groups())
print(m2.group(0))
print(m2.group(1))
print(m2.group(2))
print(m2.group(3))

print('\n贪婪匹配')
m3=re.match(r'^(\d+)(0*)$', '1230560078000')
print(m3.groups())
print(m3.group(2))

m4=re.match(r'^(\d+?)(0*)$', '1230560078000')
print(m4.groups())
print(m4.group(2))

print('\n预编译正则表达式')
re_telephone=re.compile(r'^(\d{3,4})(-|\s+)(\d{6,8})$')
m5 = re_telephone.match('32323-3423243234233')
print(m5)
m5 = re_telephone.match('0668   5585569')
print(m5.groups())
m5 = re_telephone.match('10668   5585569')
print(m5)

print(('\n请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：'
		'someone@gmail.com bill.gates@microsoft.com'))
m8=re.match(r'^((\w|\.)*)(@(\w*)\.(\w+))$', 'someone@gmail.com')
print(m8.groups())
m9=re.match(r'^((\w|\.)*)(@(\w*)\.(\w+))$', 'bill.gates@microsoft.com')
print(m9.groups())
		
print('\n版本二可以提取出带名字的Email地址：\n'
		'<Tom Paris> tom@voyager.org => Tom Paris'
		'bob@example.com => bob')

mat=r'^(\w+)(@\w+\.\w*)$'
matEx=r'<(.+?)>\s*(\w+)(@\w+\.\w*)$'

def matchFun(str):
	r1=re.match(mat, str)
	if r1:
		print(r1.groups(), r1.group(1))
	else:
		r1 = re.match(matEx, str)
		if r1:
			print(r1.groups(), r1.group(1))
		else:
			print('no valid email address')


matchFun('<Tom Paris> tom@voyager.org')
matchFun('bob@example.com')
