# _*_ coding:utf-8 _*_

g=(x for x in range(10,20))
print(g)

print(next(g))
print(next(g))
print(next(g))

for x in g:
	print(x)
	
print('著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：')

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
	
fib(10)

print('要把fib函数变成generator，只需要把print(b)改为yield b就可以了：')
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
	
yie = fib2(5)
print(next(yie))
for x in fib2(10):
	print(x)
	

print('捕获StopIteration错误')
def dequeValue(x):
	a = 0
	while a < x:
		yield a
		a = a + 1
	return 'end'

val = dequeValue(5)
while True:
	try:
		print(next(val))
	except StopIteration as e:
		print("Generator return value:", e.value)
		break
		
		
	