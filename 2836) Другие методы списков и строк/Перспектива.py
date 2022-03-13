a = [int(k) for k in input().split()]
p = a[0]
o = [a[0]]
for r in a:
    if r > p:
        o.append(r)
        p = r
print(*o, sep='>>')

