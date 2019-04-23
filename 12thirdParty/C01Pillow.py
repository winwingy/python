#_*_coding=utf-8_*_=
from PIL import Image
im=Image.open('test.png')
w,h=im.size
print('Original image size:%sx%s' %(w, h))
im.thumbnail((w/2, h/2))
print('Resize image to : %sx%s' % (w/2, w/2))
im.save('thumbnail.png', 'png')

print('\n 模糊效果也只需几行代码：')
from PIL import ImageFilter

im = Image.open('test.png')
im2=im.filter(ImageFilter.BLUR)
im2.save('blur.png', 'png')


print('\n 生成字母验证码图片：')
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def rndChar():
	return chr(random.randint(65, 90))
	
def rndColor():
	return (random.randint(64, 255), random.randint(64, 255), random.randint(64,255))
	
def rndColor2():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(23, 127))
	
def rndColor3():
	return (255, 255, 0)
	
width=60*4
height=60
image=Image.new('RGB', (width, height), (255, 255, 255))
font=ImageFont.truetype('SIMLI.TTF', 36)
#font=ImageFont.Load_default()
#创建draw对象
draw=ImageDraw.Draw(image)
for x in range(width):
	for y in range(height):
		draw.point((x, y), fill=rndColor())
		
for t in range(4):
	draw.text((60*t+10, 10), rndChar(), font=font, fill=rndColor2())
	
image=image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')



