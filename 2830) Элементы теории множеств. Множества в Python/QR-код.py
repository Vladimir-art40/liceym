i = []
p = set()

while (k := input()) != '':
    i.append(k)

while (k := input()) != '':
    i.append(k)

while (k := input()) != '':
    i.append(k)

e = int(input())
for h in range(e):
    qw = input()
    if qw in i and qw not in p:
        print(qw)
        p.add(qw)

