# _*_ coding:utf-8 _*_

def fact(n):
	if n == 1:
		return 1
	return n*fact(n-1)
	
print(fact(10))

print('递归太多导致栈溢出')
#print(fact(1000))


print('尾递归优化')
def factGood(n):
	return factGood_impl(n, 1)
	
def factGood_impl(n, sum):
	if n == 1:
		return sum
	return factGood_impl(n-1, sum*n)
	
print(factGood(5))
print('python没有做尾递归优化')
#print(factGood(1000))
	