a = [int(k) for k in input().split()]
p = [a]
while len(p[-1]) > 1:
    work = p[-1]
    new = []
    for i in range(0, len(work), 2):
        if i + 1 < len(work):
            new.append(work[i] + work[i + 1])
        else:
            new.append(work[i])
    p.append(new)

for i in range(len(p)):
    t = p[len(p) - i - 1]
    print(*t)

