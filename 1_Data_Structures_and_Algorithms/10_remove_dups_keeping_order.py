# remove duplicate but maintain the order

def dedup(items):
 seen=set()
 for item in items:
  if item not in seen:
   yield item
   seen.add(item)

a=[1,4,3,1,6,4,2,1]
b=list(dedup(a))
# print(b)

def dedupe(items,key=None):
 seen=set()
 for item in items:
  val=item if key is None else key(item)
  if val not in seen:
   yield item
   seen.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]