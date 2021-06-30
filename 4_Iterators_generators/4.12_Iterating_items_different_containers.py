from itertools import chain
a=[1,2,3,4]
b=['x','z']

for x in chain(a,b):
 print(x,end=' ')