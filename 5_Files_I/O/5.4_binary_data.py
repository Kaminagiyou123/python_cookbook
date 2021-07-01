# with open('somefile.bin','rb') as f:
#  data=f.read()
 
# with open('somefile.bin','wb') as f:
#  f.write(b'hello world')
 
t='Hello World'
print(t[0])

b=b'hello world'
print(b[0])

import array
nums=array.array('i',[1,2,3,4])
with open('data.bin','wb') as f:
 f.write(nums)