with open('somefile.txt','rt') as f:
 data=f.read()
 
with open('somefile.txt','rt') as f:
 for line in f:
  print(line)
  
with open('somefile.txt','wt') as f:
 f.write(text1)
 f.write(text2)
 
with open('somefile.txt','wt') as f:
 print(line1,file=f)
 print(line2,file=f)