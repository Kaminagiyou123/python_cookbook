def count(n):
 while True:
  yield n
  n+=1
  
c=count(0)

import itertools
for x in itertools.islice(c,10,15):
 print(x)

print('-' *20)
print(next(c))
print(next(c))