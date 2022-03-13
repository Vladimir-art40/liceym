s = int(input())
o = set()
for i in range(1, int(s ** 0.5) + 1):
    if s % i == 0:
        o.add(s // i)
        o.add(i)
print(*sorted(o))

