#_*_coding=utf-8_*_=
import struct

b1 = struct.pack('>I',0x01000002)
print(b1)

a1=10240099
b1 = struct.pack('>I',a1)
print(b1)

u1 = struct.unpack('>I',b1)
print(u1)

u1 = struct.pack('>H', 1000)
print(u1)

print('\n 请编写一个bmpinfo.py，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。')
import base64, struct
bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')
print(len(bmp_data))

def getBmpInfo(bmp_data):
	li = struct.unpack('<ccIIIIIIHH', bmp_data[0:30])
	print(li)
	ret = False
	while True:
		if len(li)!=10:
			break
			
		if (li[0]!=b'B' or li[1]!=b'M' or li[3]!=0 or li[8]!=1):
			break
		return True,li[6],li[7],li[9]
		
	return ret,0,0,0

ret,width,height,color = getBmpInfo(bmp_data)
print(ret, 'width=', width, 'height=', height, 'color=', color)