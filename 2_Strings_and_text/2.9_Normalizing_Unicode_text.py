s1='Spicy Jalape\u00f1o'
s2="Spicy Jalapen\u0303o"
print(len(s1))
print(len(s2))

import unicodedata
t1=unicodedata.normalize('NFC',s1)
t2=unicodedata.normalize('NFC',s2)
print(ascii(t1))
print(ascii(t2))

t1=unicodedata.normalize('NFD',s1)
t2=unicodedata.normalize('NFD',s2)
print(ascii(t1))
print(ascii(t2))

t1=unicodedata.normalize('NFD',s1)
t1_new=''.join(c for c in t1 if not unicodedata.combining(c))
print(t1_new)