n = int(input())
k = [0] * n
for e in range(n):
    u = [0] * 11
    for i in range(11):
        u[i] = int(input())
    k[e] = u
h = []
for t in range(11):
    p = 0
    r = 0
    for i in range(n):
        if k[i][t] != 0:
            p += k[i][t]
            r += 1
    if r == 0:
        continue
    h.append((p / r, t + 1))

print(min(h)[1], max(h)[1])

