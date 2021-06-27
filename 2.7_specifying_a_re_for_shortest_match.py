import re
str_pat=re.compile(r'\"(.*)\"')
text1= 'Computer says "No"'
text1_new=str_pat.findall(text1)
print(text1_new)

text2= 'Computer says "No" Phone says"Yes"'
text2_new=str_pat.findall(text2)
print(text2_new)

str_pat_2 = re.compile(r'\"(.*?)\"')
text3= 'Computer says "No" Phone says"Yes"'
text3_new=str_pat.findall(text3)
print(text3_new)