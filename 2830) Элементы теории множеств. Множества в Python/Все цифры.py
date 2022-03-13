a = input()
p = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for u in a:
    if int(u) in p:
        p.remove(int(u))

for g in p:
    print(g, end=' ')

