# mapping keys to multiple values in a dictionary
from collections import defaultdict

d={
 'a':[1,2,3],
 'b':[4,5]
}

e={
 'a':{1,2,3},
 'b':[4,5]
}

d=defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

e=defaultdict(set)
e['a'].add(1)
e['a'].add(2)
e['b'].add(4)

d={}
for key,value in pairs:
 if key not in d:
  d[key]=[]
d[key].append(value)

d=defaultdict(list)
for key,value in pairs:
 d[key].append(value)
 
