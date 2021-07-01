import os
names=os.listdir('5_Files_I')

import os.path
names=[name for name in os.listdir('5_Files_I')
       if os.path.isfile(os.path.join('5_Files_I',name))]

print(names)

names=[name for name in os.listdir('5_Files_I')
       if os.path.isdir(os.path.join('5_Files_I',name))]

print(names)

pyfiles=[name for name in os.listdir('5_Files_I')
         if name.endswith('.py')]



from fnmatch import fnmatch
pyfiles=[name for name in os.listdir('5_Files_I')
         if fnmatch(name,'*.py')]

print(pyfiles)