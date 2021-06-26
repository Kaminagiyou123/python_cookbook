from collections import ChainMap
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
c=ChainMap(a,b)
print(c['z'])
a['x']=32
print(c)

values=ChainMap()
values['x']=1
values=values.new_child()
values['x']=2
values=values.new_child()
values['x']=3

print(values['x'])
values=values.parents
print(values['x'])
values=values.parents
print(values['x'])