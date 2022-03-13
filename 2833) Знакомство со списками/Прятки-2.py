n = int(input())
p = []
for h in range(n):
    p.append(input())
m = int(input())
find = []
for h in range(m):
    find.append(input())
for k in p:
    op = True
    for fw in find:
        if fw not in k:
            op = False
    if op:
        print(k)

