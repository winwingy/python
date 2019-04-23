#_*_coding=utf-8_*_
import pickle
print('\n\n 序列化')
d = dict(name='bob', age=12)
ed = pickle.dumps(d)
print(ed)

d2 = pickle.loads(ed)

print(d2)

with open('dump.txt', 'wb') as f:
	pickle.dump(d, f)
	
with open('dump.txt', 'rb') as f:
	d3=pickle.load(f)
	print(d3)
	
print('\n\njson pickling')
import json

d=dict(name='tom', age=20)
d2=json.dumps(d)
print(d2)
d3 = json.loads(d2)
print(d3)


print('\n\n JSON进阶')
class Student(object):
	def __init__(self, name,age):
		self.name=name
		self.age=age
		
s=Student('lily',5)
#毫不留情地得到一个TypeError：
#sd=json.dumps(s)
#print(sd)

def student2dict(stu):
	return {'name':stu.name,'age':stu.age}
	
sd2=json.dumps(s, default=student2dict)
print(sd2)

def dict2student(di):
	return Student(di['name'], di['age'])
	
se2=json.loads(sd2, object_hook=dict2student)
print(se2)

