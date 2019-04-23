# _*_ coding:utf-8 _*_

print('按绝对值大小排序：')

li = [1, 5, -10, 9, -3]

print(sorted(li))
print(sorted(li, key=abs))


print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))


print('tuple表示学生名字和成绩：按名字排序：')
li2 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

li3 = sorted(li2)
print(li3)

def byScore(x):
	return x[1]
	
li4 = sorted(li2, key=byScore)
print(li4)