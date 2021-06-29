from datetime import timedelta
a=timedelta(days=2,hours=4)
b=timedelta(hours=8)
c=a+b
print(c)
print(c.days)
print(c.seconds)
print(c.total_seconds())

from datetime import datetime
now=datetime.now()
print(now+timedelta(minutes=30))
