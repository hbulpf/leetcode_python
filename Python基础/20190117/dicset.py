ad = {'mar': 13, (1,2):55,'wat': 67}
ad['hap'] = 23
print(ad)
print(ad['wat'])
print(ad.get('pap'))
print(ad.get('pap',1))
print(ad)
ad.pop('mar')
print(ad)

s = set([2,2,3,(1,2),5])
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)
se = set([5,2,(2,3)])
print(se & s)
print(se | s)
