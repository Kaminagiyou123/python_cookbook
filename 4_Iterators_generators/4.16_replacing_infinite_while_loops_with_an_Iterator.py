CHUNKSIZE=8192
def reader(s):
 while True:
  data=s.recv(CHUNKSIZE)
  if data==b'':
   break
  process_data(data)