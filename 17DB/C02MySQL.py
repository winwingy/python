#_*_coding=utf-8_*_=

import mysql.connector

#先删除同名录下的test.db

#conn = mysql.connector.connect(user='root', password='password', database='test')
conn = mysql.connector.connect(user='root', password='password', database='test2')
cursor = conn.cursor()

cursor.execute('drop table user2')

cursor.execute('create table user2 (id varchar(20) primary key, name varchar(20), sex varchar(20))')

cursor.execute('insert into user2 (id, name, sex) values (%s, %s, %s)', ['1', 'Michael', 'man'])
cursor.execute('insert into user2 (id, name, sex) values (%s, %s, %s)', ['2', 'jim', 'man'])
print(cursor.rowcount)

conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from user2 where id = %s', ('1',))
values = cursor.fetchall()
print(values)

cursor.execute('select * from user2 where sex = %s', ('man',))
values = cursor.fetchall()
print(values)


cursor.close()

conn.close()

