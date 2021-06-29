from datetime import datetime
text='2012-09-20'
y=datetime.strptime(text,'%Y-%m-%d')
z=datetime.now()
diff=z-y
print(diff)
print(datetime.strftime(z,'%A %B %d, %Y'))

from datetime import datetime
def parse_ymd(s):
 year_s,mon_s,day_s=s.split("-")
 return datetime(int(year_s),int(mon_s),int(day_s))