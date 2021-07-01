import io
s=io.StringIO()
print(s.write('Hello world\n'))
print('this is a test',file=s)
print(s.getvalue())

a=io.StringIO('hello\nworld\n')
print(a.read(4))
print(a.read())

s=io.BytesIO()
s.write(b'binary data')
print(s.getvalue())
