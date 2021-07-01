from tempfile import TemporaryFile
from tempfile import NamedTemporaryFile
from tempfile import TemporaryDirectory

with TemporaryFile('w+t') as f:
 f.write('Hello world\n')
 f.write('Testing\n')
 f.seek(0)
 data=f.read()
 print(data)
 f.close()
 
with NamedTemporaryFile('w+t') as f:
 print('filename is :'+f.name)
 f.close()
 
with TemporaryDirectory() as dirname:
 print('dirname is : '+dirname)