import os
print(os.path.exists('data.bin'))
print(os.path.exists('tt.bin'))

print(os.path.isfile('data.bin'))
print(os.path.isdir('data.bin'))
print(os.path.islink('data.bin'))
print(os.path.realpath('data.bin'))


print(os.path.getsize('data.bin'))
import time
print(time.ctime(os.path.getmtime('data.bin')))