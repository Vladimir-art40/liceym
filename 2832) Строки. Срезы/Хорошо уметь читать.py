a = input()
r = ['E', 'S', 'M']
e = 0
o = 0
lo = -1
for h in a:
    o += 1
    if h in r:
        print(o - lo - 1)
        lo = o
        e += 1
    if e == 2:
        break

if e == 0:
    print(0)
    print(len(a))
elif e == 1:
    print(len(a) - lo)

t = len(set(a))
if ' ' in a:
    t -= 1
if 'E' in a:
    t -= 1
if 'S' in a:
    t -= 1
if 'M' in a:
    t -= 1

print(t)

