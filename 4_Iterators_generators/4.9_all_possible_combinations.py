items=['a','b','c']
from itertools import combinations_with_replacement, permutations
for p in permutations(items):
 print(p)
print('-'*40)
for p in permutations(items,2):
 print(p)
 
print('-'*40)
from itertools import combinations
for p in combinations(items,3):
 print(p)

print('-'*40) 
for p in combinations(items,2):
 print(p)

print('-'*40) 
for p in combinations_with_replacement(items,3):
 print(p)