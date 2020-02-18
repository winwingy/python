#_*_coding=utf-8_*_=

from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker,  relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


'''
### 基本用法 ####
class User(Base):
	__tablename__='user'
	id = Column(String(20), primary_key=True)
	name=Column(String(20))
	
engine = create_engine('mysql+mysqlconnector://root:password@localhost/test')
DBSession = sessionmaker(bind=engine)

#创建session对象
session = DBSession()
#创建新的User对象：
new_user = User(id='22', name='Bob2')
#添加到session:
session.add(new_user)
#提交即保存到数据库：
session.commit()
#关闭session:
session.close()

####查询数据
#创建Session:
session = DBSession()
#创建Query查询， filter是where条伯，最后调用one()返回唯一行，
#如果调用all()则返回所有行：
user = session.query(User).filter(User.name=='Bob2').all()
#打印类型和对象的name属性：
print('type:', type(user))
for one in user:
	print('name:%s id:%s'% (one.name, one.id))

session.close()

'''


##### User拥有多个Book ####
class Group(Base):
	__tablename__ = 't_group'
	
	id = Column(Integer, primary_key=True)
	name = Column(String(20))
	#一对多：
	users =  relationship('User')
	
class User(Base):
	__tablename__ = 't_user'
	
	id = Column(Integer, primary_key=True)
	name = Column(String(20))
	# "多"的一方的book表是通过外键关联到user表的：
	groupid = Column(Integer, ForeignKey('t_group.id'))
	
engine = create_engine('mysql+mysqlconnector://root:password@localhost/test2')
DBSession = sessionmaker(bind=engine)

#创建Group
session = DBSession()
groups = session.query(Group)
for one in groups:
	session.delete(one)
	
group = Group(1, 'Group1')
session.add(group)
group = Group(2, 'Group2')
session.add(group)
session.commit()
groups = session.query(Group)
print("group has: \n")
for one in groups:
	print(one, " ")
	
session.close()


#创建user
session = DBSession()
users = session.query(User)
for one in users:
  session.delete(one)
  
user = User(id=1, name='jim', groupid=1)
session.add(user)
user = User(id=2, name='tom', groupid=2)
session.add(user)
session.commit()
session.close()

