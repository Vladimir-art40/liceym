s = input()
r = input().split()
for t in r:
    print(*[h.upper() for h in t], sep=s, end=' ')

