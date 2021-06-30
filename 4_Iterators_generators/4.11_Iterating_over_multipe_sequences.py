xpts=[1,5,4,2,10,7]
ypts=[101,78,37,15,62,99]

for x,y in zip(xpts,ypts):
 print(x,y)
 
print('*'*20)

a=[1,2,3]
b=['x','y','z','m']

for a,b in zip(a,b):
 print(a,b)
 
from itertools import zip_longest
print('*'*20)
a=[1,2,3]
b=['x','y','z','m']
for x,y in zip_longest(a,b):
 print(x,y)
 
print('*'*20)
a=[1,2,3]
b=['x','y','z','m']
for x,y in zip_longest(a,b,fillvalue=0):
 print(x,y)
 
 
print('*'*20)

a=[1,2,3]
b=[10,11,12]
c=['x','y','z']

for x,y,z in zip(a,b,c):
 print(x,y,z)
 
print(zip(a,b,c))
print(list(zip(a,b,c)))