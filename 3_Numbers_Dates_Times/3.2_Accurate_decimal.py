a=4.2
b=2.1
print(a+b)
print(a+b==6.3)

from decimal import Decimal,localcontext

a=Decimal('5.2')
b=Decimal('2.3')
print(a+b)

with localcontext() as ctx:
 ctx.prec=3
 print(a/b)
 
 with localcontext() as ctx:
  ctx.prec=49
  print(a/b)