from fractions import Fraction

a=Fraction(4,3)
b=Fraction(3,4)
c=a*b
d=a/b
print(a/b)
print(a.numerator)
print(a.denominator)
print(d)
print(float(d))
print(d.limit_denominator(2))
e=3.444
print(*e.as_integer_ratio())