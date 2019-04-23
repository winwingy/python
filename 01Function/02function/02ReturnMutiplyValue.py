# _*_ coding:utf-8 _*_

import math

def move(x, y, step, angle=0):
	nx = x + step*math.cos(angle)
	ny = x - step*math.sin(angle)
	return nx,ny

x,y=move(1, 2, 2)
print(x,y)

print('return one tuple')
val=move(1, 2, 2)
print(val)