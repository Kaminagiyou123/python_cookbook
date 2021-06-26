# unpacking works with any object that happens to be iterable
# Unpacking a Sequence into Seperate Varibles
p=(4,5)
x,y=p

data=['ACME',50,91.1,(2012,12,21)]
name,shares,price,date=data
name,shares,price,(year,month,day)=data

s="hello"
a,b,c,d,e=s

data=[_,shares,price,_]=data
# Unpacking Elments from Iterables of Aribtrary

