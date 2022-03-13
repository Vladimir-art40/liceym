def f(d):
    o = 1
    if d % 2 == 0:
        o += 1
    out = 1
    for h in range(o, d + 1, 2):
        out *= h
    return out


n = int(input())
y = []
for t in range(n + 1):
    y.append((t, f(t)))
print(y)

