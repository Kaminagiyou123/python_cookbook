def frange(start,stop,increment):
 x=start
 while x< stop:
  yield x
  x+=increment
 
print(next(frange(0,4,0.5)))
for n in frange(0,4,0.5):
 print(n)

def countdown(n):
 print('start countdown from', n)
 while n>0:
  yield n
  n-=1

for n in countdown(3):
 print(n)