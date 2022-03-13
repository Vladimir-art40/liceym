p = []
a = input()
q = '*+ox-<'
while a != '':
    p.append(a.split(', '))
    a = input()
n = len(p)
m = len(p[0])
mx = 0
for j in range(m):
    s = 0
    for i in range(n):
        s += int(p[i][j])
    mx = max(s, mx)
out = [[' ' for _ in range(mx)] for _ in range(m)]
for j in range(m):
    poz = 0
    f = 0
    for i in range(n):
        for num in range(int(p[i][j])):
            out[j][poz] = q[f % 6]
            poz += 1
        f += 1
for j in range(mx - 1, -1, -1):
    for i in range(m):
        print(out[i][j] * 2, end=' ')
    print()
    

