p = input()
t = len(set(p)) <= 32
smin = ord(p[0])
smax = ord(p[0])
for u in p:
    smin = min(smin, ord(u))
    smax = max(smax, ord(u))
print(smin, smax, sep=', ')
if t:
    print('ХВАТИТ')
else:
    print('НЕ ХВАТИТ')

