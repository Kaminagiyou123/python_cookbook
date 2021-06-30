with open('/etc/passwd') as f:
 try:
  while True:
   line=next(f)
   print(line, end='')
  
 except StopIteration:
  pass
   
items=[1,2,3]
it=iter(items)
print(next(it))
print(next(it))
print(next(it))