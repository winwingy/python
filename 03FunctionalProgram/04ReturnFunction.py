# _*_ coding:utf-8 _*_


def sumCount(*args):
	def sumC():
		cnt=0
		for x in args:
			cnt = cnt + x
		return cnt
	return sumC
	

f = sumCount(1, 2, 3)
print(f())


print('返回的函数并没有立刻执行，而是直到调用了f()才执行 以下就出现自己想不到的效果')

def count1():
	fs=[]
	for i in range(1, 4):
		def f():
			return i*i
		fs.append(f)
	return fs
	
f1,f2,f3=count1()
print(f1(),f2(), f3())


print('返回的函数并没有立刻执行，而是直到调用了f()才执行 改进版')


def count2():
	fs=[]
	
	def fw(x):
		def f():			
			return x*10
		return f
	
	for i in range(1, 4):		
		fs.append(fw(i))
	return fs
	
f1,f2,f3=count2()
print(f1(),f2(), f3())

print('\n 利用闭包返回一个计数器函数，每次调用它返回递增整数：')


def addCount():
	li = [1]
	def addOut():	
		li[0] = li[0] + 1
		return li[0]
	return addOut
	
	
f4=addCount()
print(f4())
print(f4())
print(f4())
print(f4())
	

