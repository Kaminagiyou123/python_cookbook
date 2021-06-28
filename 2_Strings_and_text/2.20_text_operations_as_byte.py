data=b'Hello world'
print(data[0:5])
print(data.startswith(b'Hello'))
print(data[0])
print(data[1])
print(data.decode('ascii'))

data='Hello world'
print(data[0:5])
print(data.startswith('Hello'))
print(data.split(" "))
print(data[0])
print(data[1])