n = int(input())
m = int(input())
p = []
for i in range(n):
    line = []
    for j in range(m):
        line.append(input())
    p.append(line)


for i in p:
    print(*i, sep='; ')
    
print()

for j in range(m):
    out = []
    for i in range(n):
        out.append(p[i][j])
    print(*out, sep='; ')


