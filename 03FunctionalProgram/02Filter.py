# _*_ coding:utf-8 _*_

print('回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：')

it = list(range(100, 500))

def isRevese(x):
	n = 0
	while n <= len(x)/2:
		if x[n] != x[-n-1]:
			return False
		n = n + 1
	return True
	
	
StrIntS=['0','1','2','3','4','5','6','7','8','9']
	
# 12345
def intToStr2(x):
	str=''
	a = StrIntS[5]		
	while True:
		inx = x - x//10*10
		#print(inx)
		str = StrIntS[inx] + str
		x = x//10
		if x <= 0:
			break
	return str
	
#print(intToStr2(12345))

li2 = map(intToStr2, it)
li3 = filter(isRevese, li2)
print(list(li3))