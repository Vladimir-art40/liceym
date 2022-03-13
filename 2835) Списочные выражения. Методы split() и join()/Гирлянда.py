a = input().split()
g = [0] * (len(max(a, key=len)) * 2 + 1)
for k in range(len(g)):
    h = [' '] * (len(a) * 2 + 1)
    if k == 0 or k == len(g) - 1:
        for u in range(0, len(h), 2):
            h[u] = '_'
    g[k] = h

poz = 1
for step in a:
    for t in range(len(step)):
        g[t][poz] = step[t]
        g[len(g) - t - 1][poz] = step[t]
    poz += 2

for i in range(len(g)):
    for j in range(len(g[i])):
        print(g[i][j], end='')
    print()

