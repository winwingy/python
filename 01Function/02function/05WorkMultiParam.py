# _*_ coding:utf-8 _*_


print('以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：')

def product(x, *args):
	sum = x
	for per in args:
		sum = sum * per 
	return sum
	
print(product(1))
print(product(1, 2))

kks=(2, 3, 4)
print(product(1, *kks))

def product2(x, **args):
	print(x, args)
	
product2('a')
product2('b', kk='aa', bb='22')

dict2={'name':'lily','age':15}
product2('ddd', **dict2)
