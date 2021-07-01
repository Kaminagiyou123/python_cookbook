import gzip
with gzip.open('somefile.gz','rt') as f:
 text=f.read()
with gzip.open('somefile.gz','wt') as f:
 text=f.write(text)
 
import bz2
with bz2.open('somefile.gz','rt') as f:
 text=f.read()
with bz2.open('somefile.gz','wt') as f:
 text=f.write(text)