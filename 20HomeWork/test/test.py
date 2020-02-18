#_*_coding=utf-8_*_=

li = [1, 2, 3, 4, 5]
liret = map(lambda x : x*10, li)
print(list(liret))


from functools import reduce

reRet = reduce(lambda x,y : x + y + 10, li)
print(reRet)


