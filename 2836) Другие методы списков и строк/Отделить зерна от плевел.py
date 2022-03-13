f = input().split()

for step in f:
    t = [e.lower() for e in step if e.isalpha()]
    if len(t) == 0:
        continue
    t[0] = t[0].upper()
    print(*t, sep='', end=' ')
print()

for step in f:
    t = [e for e in step if not e.isalpha()]
    if len(t) == 0:
        continue
    t[0] = t[0].upper()
    print(*t, sep='', end=' ')

