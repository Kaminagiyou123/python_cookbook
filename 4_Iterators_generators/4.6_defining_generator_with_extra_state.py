from collections import deque

class linehistory:
 def __init__(self,lines,hislen=3):
  self.lines=lines
  self.history=deque(maxlen=hislen)
  
 def __iter__(self):
  for lineno,line in enumerate(self.lines,1):
   self.history.append((lineno,line))
   yield line
   
 def clear(self):
  self.history.clear()