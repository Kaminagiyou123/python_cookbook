from fnmatch import fnmatch,fnmatchcase
print(fnmatch('foo.txt','*.txt'))
print(fnmatch('foo.txt','?**.txt'))
print(fnmatch('Dat45.csv','Dat[0-9]*'))

names=['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
ns=[x for x in names if fnmatch(x,'Dat*.csv')]
print(ns)

print(fnmatchcase('foo.txt','.TXT'))

addresses = [
        '5412 N CLARK ST',
        '1060 W ADDISON ST',
        '1039 W GRANVILLE AVE',
        '2122 N CLARK ST',
        '4802 N BROADWAY',
]

addresses_new=[x for x in addresses if fnmatch(x,'*ST')]
print(addresses_new)

address_new2=[x for x in addresses if fnmatch(x,'54[0-9][0-9] *CLARK*')]
print(address_new2)
