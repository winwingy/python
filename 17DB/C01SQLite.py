#_*_coding=utf-8_*_=
import sqlite3

conn=sqlite3.connect('test.db')
cursor = conn.cursor()
try:
	ret = cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
	print(ret)
	ret = cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
	print(ret)
except BaseException as e:
	print(e)

print(cursor.rowcount)
cursor.close()
conn.commit()
conn.close()


print('\n 试试查询记录')
conn = sqlite3.connect('test.db')
cursor= conn.cursor()
cursor.execute('select * from user where id=?', ('1',))
print(cursor.fetchall())
cursor.close()
conn.close()


print(' \n 请编写函数，在Sqlite中根据分数段查找指定的名字:')
import os,sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'work.db')
if os.path.isfile(db_file):
	os.remove(db_file)
	
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name var char(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute(r'select * from user where score between ? and ? order by score', (low, high))
	print(cursor.fetchall())
	
get_score_in(80, 95)
get_score_in(60, 80)
get_score_in(60, 100)
