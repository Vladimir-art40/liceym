n = int(input())
p = []
for h in range(n):
    p.append(input())
m = int(input())
for h in range(m):
    print(p[h % n])

