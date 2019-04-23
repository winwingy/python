#_*_coding=utf-8_*_
from datetime import datetime
dt = datetime.now()
print(dt)
dt2=datetime(2050,1,1,9,11,11)
print(dt2)
t = dt.timestamp()
print(t)
dt3=datetime.fromtimestamp(t)
print(dt3)
dt5=datetime.utcfromtimestamp(t)
print(dt5)

dt6 = datetime.strptime('2018-5-1 1:2:3', '%Y-%m-%d %H:%M:%S')
print(dt6)

str = dt6.strftime('%H:%M:%S')
print(str)

print('\n 时间运算')
from datetime import timedelta
dt7 = datetime.now() + timedelta(days=5)
print(dt7)
td=dt7-datetime.now()
print(td)

from datetime import timezone
tz_utc_8=timezone(timedelta(hours=8))
now=datetime.now()
print(now)
dt=now.replace(tzinfo=tz_utc_8)
print(dt)

print('\n时区转换')
utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
tokyo_dt=bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)

print('\n 假设你获取了用户输入的日期和时间如2015-1-21  \n'
' 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：')
dt = datetime.strptime('2015-1-21 9:01:30', '%Y-%m-%d %H:%M:%S')
dt.replace(tzinfo=timezone(timedelta(hours=5)))
print(dt)
print(dt.timestamp())