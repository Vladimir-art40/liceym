a = int(input())


def Factor(n):
    Ans = []
    asd = 2
    while asd * asd <= n:
        if n % asd == 0:
            Ans.append(asd)
            n //= asd
        else:
            asd += 1
    if n > 1:
        Ans.append(n)
    return Ans


d = Factor(a)
out = 1
f = []
for g in d:
    if not (g in f):
        out *= g
        f.append(g)
print(int(out))

