s='{name} has {n} messages'
print(s.format(name='Guido', n=37))

name='Guido'
n=37

print(s.format_map(vars()))

class Info:
 def __init__(self,name,n):
  self.name=name
  self.n=n

a=Info(name="Guido",n=37)
print(s.format_map(vars(a)))

class safesub(dict):
 def __missing__(self,key):
  return '{'+key+'}'
del n
print(s.format_map(safesub(vars())))

import sys

def sub(text):
 return text.format_map(safesub(sys._getframe(1).f_locals))

name='Guido'
n=37
print(sub("hello {name}"))
print(sub('you have {n} messages '))
print(sub('Your fav color is {color}'))

