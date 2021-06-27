import re
comment=re.compile(r'/\*(.*?)\*/')
text1='/*this is a comment*/'
print(comment.findall(text1))

text2='''/*this is a 
multiline comment*/'''

comment_2=re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment_2.findall(text2))

comment_3=re.compile(r'/\*(.*?)\*/',re.DOTALL)
print(comment_3.findall(text2))