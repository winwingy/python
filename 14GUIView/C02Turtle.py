#_*_coding=utf-8_*_=
from turtle import *

'''
width(4)

forward(200)
right(90)

pencolor('red')
forward(100)
right(90)

pencolor('green')
forward(200)
right(90)

pencolor('blue')
forward(100)
right(90)

done()
'''


print('\n 画五角星')
def drawStar(x, y):
	pu()
	goto(x,y)
	pd()
	#set heading:0
	seth(0)
	for x in range(5):
		fd(40)
		rt(144)
		
for x in range(0, 250, 50):
	drawStar(x, 0)
	
done()
