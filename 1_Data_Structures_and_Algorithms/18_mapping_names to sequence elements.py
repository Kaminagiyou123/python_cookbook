from collections import namedtuple

Subscriber=namedtuple("Subscriber",['addr','joined'])
sub=Subscriber('jonesy@example.come','2012-10-19')
# print(sub.joined)
# print(sub.addr)

sub2=Subscriber(addr='ranyou@gmail.com',joined='2021-01-01')
addr,joined=sub2

# print(joined)
Stock = namedtuple('Stock', ['name', 'shares', 'price'])

def compute_cost(records):
 total=0.0
 for rec in records:
  s=Stock(*rec)
  total+=s.shares*s.price
 return total

s=Stock('ACME',shares=100,price=123.45) 
s=s._replace(price=75) #new tuple made
print(s)

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype=Stock("",0,0.0,None,None)
def dict_to_stock(s):
 return stock_prototype._replace(**s)

a={'name':"ACME",'shares':100,'price':123.45}
print(dict_to_stock(a))
b={'name':'ACME','shares':100,'price':123.45,'date':'12/17/2012'}
print(dict_to_stock(b))