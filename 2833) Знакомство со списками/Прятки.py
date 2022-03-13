n = int(input())
p = []
for h in range(n):
    p.append(input())
m = int(input())
for h in range(m):
    w = input()
    g = -1
    for e in range(n):
        if w in p[e]:
            if g == -1:
                g = e + 1
    print(g)

