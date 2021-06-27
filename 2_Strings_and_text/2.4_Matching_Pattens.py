text = 'yeah, but no, but yeah, but no, but yeah'
print(text=='yeah')
print(text.startswith('yeah'))
print(text.endswith('no'))
print(text.find('no'))

import re
text1='11/27/2012'
text2='Nov 27,2012'
if re.match(r'\d+/\d+/\d+',text2):
 print('yes')
else:
 print('no')

datepat=re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
 print('yes')
else:
 print('No')
 
if datepat.match(text2):
  print('yes')
else:
 print('No')
 
 text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
 
print(datepat.findall(text))


for m in datepat.finditer(text):
 print(m.group(0))
 
print(re.findall(r'\d+/\d+/\d+',text))