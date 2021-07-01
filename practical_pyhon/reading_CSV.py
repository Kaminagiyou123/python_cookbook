import csv
def parse_csv(filename,select=None, types=None,has_headers=False,silence_errors=True):
 with open(filename) as f:
    rows=csv.reader(f)
    if has_headers==True:
      headers=next(rows)
    if select:
      indices=[headers.index(colname) for colname in select]
      headers=select
    else:
      indices=[]
    records=[]
    for row in rows:
      try: 
        if not row:
          continue
        if indices:
          row=[row[index] for index in indices]
        if types:
          row = [func(val) for func, val in zip(types, row) ]
        if headers:
          record=dict(zip(headers,row))
        else:
          record=dict(row)
        records.append(record)
      except ValueError as e:
        if silence_errors==True:
         pass
        else:
          print(e)
          raise
       
    return records
  


print(parse_csv('practical_pyhon/missing.csv',select=['name','shares','price'],types=[str,int,float],has_headers=True,silence_errors=True))