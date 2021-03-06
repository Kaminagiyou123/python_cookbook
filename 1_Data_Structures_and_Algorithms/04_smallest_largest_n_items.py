# finding the largest or smallest N items

import heapq

nums=[1,8,2,23,7,0,4,-3,232,43,2,22]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))

portfolio = [
       {'name': 'IBM', 'shares': 100, 'price': 91.1},
       {'name': 'AAPL', 'shares': 50, 'price': 543.22},
       {'name': 'FB', 'shares': 200, 'price': 21.09},
       {'name': 'HPQ', 'shares': 35, 'price': 31.75},
       {'name': 'YHOO', 'shares': 45, 'price': 16.35},
       {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap=heapq.nsmallest(3,portfolio,lambda x:x['price'])
high_share=heapq.nlargest(3,portfolio,lambda x:x['shares'])

print(cheap)
print(high_share)

nums=[1,8,2,23,7,0,4,-3,232,43,2,22]
heap=list(nums)
heapq.heapify(heap)
print(heap)