# _*_ coding:utf-8 _*_



def show(name,age,city='guangzhou',hometown='guangzhou'):
	print(name,age,city, hometown)
	
show('liming',15)
show('lily',20,hometown='maoming')


print('Bad example:variable as default param')

def arrAdd(arr=[]):
	arr.append('END');
	return arr;
	
a = arrAdd([1,2,3])
print(a)
b = arrAdd([4,5,6])
print(b)
c = arrAdd()
print(c)
d = arrAdd()
print(d)


print('Good example:none as default param')

def arrAddGood(arr=None):
	if arr is None:
		arr = []	
	arr.append('END')
	return arr
	
k = arrAddGood()
print(k)
j = arrAddGood()
print(j)

print('variable count param:')
def sumMy(*arrList):
	sum = 0
	for x in arrList:
		sum = sum + x
	return sum

print(sumMy(1))
print(sumMy())
print(sumMy(1, 2, 3))
lis = [4,5,6]
print(sumMy(*lis))


print('关键字参数')
def person(name,age,**other):
	print(name,age,'other:',other)
	return
	
print(person('jim', 11))
print(person('tom',20, city='guangzhou'))

lis2={'city':'maomin', 'hometown':'gaozhou'}	
print(person('lily', 25, **lis2))

print('关键字参数指定关键字/命名关键字参数')
def showStudent(name, age, **other):
	print(name,age)
	if 'hometown' in other:
		print(other['hometown'])
	if 'city' in other:
		print(other.get('city', 'guangzhou'))

		
showStudent('wj', 33, city='maoming')

def showStudent2(name, age, *, city, hometown):
	print(name, age, city, hometown)
	
showStudent2('tom', 22, city='shenzhen', hometown='shaoguan')

print('关键字参数指定关键字/命名关键字参数 : 没有传入指定的关键字')
#showStudent2('jim', 2, city='yunfu', college='shaoguan')


def showStudent3(name, age, *args, city, hometown):
	print(name, age, args, city, hometown)
	
showStudent3('lily', 33, 'good', 'skill', city='shaotou', hometown='jieyang')
showStudent3('jiaqi', 13, city='shaotou', hometown='jieyang')

def showStudent4(name, age, *args, city='guangzhou', hometown):
	print(name, age, args, city, hometown)

showStudent4('wuss', 22, hometown='beijing')
	


