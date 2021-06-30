from collections import defaultdict
from typing import DefaultDict


my_list=['a','b','c']

for idx,val in enumerate(my_list):
 print(idx,val)
 
print('**'*10)
for idx,val in enumerate(my_list,2):
 print(idx,val)
 
word_summary=defaultdict(list)
with open('myfile.txt','r') as f:
 lines=f.readlines()

for idx,line in enumerate(lines):
 words=[w.strip().lower() for w in line.split()]
 for word in words:
  word_summary[word].append(idx)