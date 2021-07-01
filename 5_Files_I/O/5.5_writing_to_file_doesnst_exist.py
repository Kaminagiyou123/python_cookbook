with open('somefile','wt') as f:
 f.write('hello\n')
 
# with open('somefile','xt') as f:
#  f.write('hello\n')
 
 
 import os
if not os.path.exists('somefile'):
  with open('somefile','wt') as f:
   f.write('hello\n')
else:
  print("file already exist!")