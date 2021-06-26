# Keeping the last N items
from collections import deque

def search(lines, pattern, history=5):
 previous_lines=deque(maxlen=history)
 for line in lines:
  if pattern in line:
   yield line, previous_lines
  previous_lines.append(line)
 

text='When writing code to search for items, it is common to use a generator function in‐ volving yield, as shown in this recipe’s solution. This decouples the process of searching from the code that uses the results. If you’re new to generators, see Recipe 4.3.'

for line,prevlines in search(text,'f',5):
 for pline in prevlines:
  print(pline,end="")
 print(line, end="")
 print('-'*20)
