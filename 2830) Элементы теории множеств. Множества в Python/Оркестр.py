a = []
b = []
c = []
all_users = set()

while (k := input()) != '':
    a.append(k)
    all_users.add(k)

while (k := input()) != '':
    b.append(k)
    all_users.add(k)

while (k := input()) != '':
    c.append(k)
    all_users.add(k)

for t in all_users:
    p = 0
    if t in a:
        p += 1
    if t in b:
        p += 1
    if t in c:
        p += 1
    if p == 1:
        print(t)

