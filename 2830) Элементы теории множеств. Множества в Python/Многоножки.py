p = int(input())
a1 = set()
a2 = set()
a3 = set()
q = set()
for t in range(p):
    h = int(input())
    q.add(h)
    if h > 40:
        a1.add(h)
    if h % 2 == 0:
        a2.add(h)
    if h % 3 == 0:
        a3.add(h)

for h in q:
    t = 0
    if h in a1:
        t += 1
    if h in a2:
        t += 1
    if h in a3:
        t += 1
    if t == 2:
        print(h, end=' ')

