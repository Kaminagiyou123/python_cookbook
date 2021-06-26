def avg(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           
    a = sum_num / len(num)
    return a
   
def drop_first_last(grades:list):
 frist,*middle,last=grades
 return avg(middle)

drop_first_last([12,66,76,86,33])

record=("Dave",'dave@gmail.com','733-234-3333','800-333-2839')
name,email,*phones=record
# print(phones)

*trailing,current=[20,4,33,4,3,22]
# print(trailing)
# print(current)

records=[('foo',1,2),
         ('bar','hello'),
         ('foo',3,5),
         ]
def do_foo(x,y):
 print('foo',x,y)

def do_bar(s):
 print('bar',s)
 
for tag,*args in records:
 if tag=='foo':
  do_foo(*args)
 elif tag=='bar':
  do_bar(*args)
 
 
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname,*fields,homedir,sh=line.split(":")

# print(uname)
# print(homedir)
# print(sh)

record = ('ACME', 50, 123.45, (12, 18, 2012))
_,*_,(*_,year)=record
# print(year)

items=[1,10,7,4,5,9]
head,*tail=items
# print(head)
# print(tail)
def sum(items):
  head,*tail=items
  return head+sum(tail) if tail else head
print(sum(items))