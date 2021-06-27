filename='spam.txt'
print(filename.endswith('.txt'))
url='http://www.python.org'
print(url.startswith("http"))

import os
filenames=os.listdir('.')
print(filenames)
print([name for name in filenames if name.startswith("1") ])
print(any(name.endswith('.py') for name in filenames))

from urllib.request import urlopen
def read_data(name):
 if name.startswith(('http:','https','ftp:')): #using a tuple
  return urlopen(name).read()
 else:
  with open(name) as f:
   return f.read()