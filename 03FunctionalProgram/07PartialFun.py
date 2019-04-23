# _*_ coding:utf-8 _*_

print('functools.partial就是帮助我们创建一个偏函数')
import functools
int16 = functools.partial(int, base=16)
print(int16('ff'))

print(int16('110', base=2))

int8 = functools.partial(int, base=8)
print(int8('77'))

print(int8('110',  base=2))


print('实际上会把10作为*args的一部分自动加到左边')
max2=functools.partial(max, 10)

print(max2(1, 100, -5))
print(max2(1))

