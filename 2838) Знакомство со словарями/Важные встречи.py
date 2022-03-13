n = int(input())
d = dict()
for _ in range(n):
    a = input().split(', ')
    month = a[2]
    if month in d:
        d[month].append((int(a[1]), a[0]))
    else:
        d[month] = [(int(a[1]), a[0])]
f = input()
t = sorted(d[f])
for line in t:
    print(line[1])

