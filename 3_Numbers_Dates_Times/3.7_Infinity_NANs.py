a=float('inf')
b=float('-inf')
c=float('nan')
import math
print(math.isinf(a))
print(math.isinf(b))
print(math.isnan(c))
print(a+34)
d=float('nan')
print(c==d)
print(c is d)
print(math.isnan(d))