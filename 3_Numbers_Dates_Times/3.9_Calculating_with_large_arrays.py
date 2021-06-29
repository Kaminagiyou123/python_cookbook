x=[1,2,3,5]
y=[3,2,3,4]
print(x*2)
print(x+y)

import numpy as np

ax=np.array([1,2,3,4])
ay=np.array([3,4,5,6])
print(ax*2)
print(ax+10)
print(ax*ay)
print(ax/ay)
print(np.sqrt(ax))
grid=np.zeros(shape=(10,10),dtype=int)
print(grid)
print(grid+10)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print(a[:,1])
print(np.where(a<10,a,10))