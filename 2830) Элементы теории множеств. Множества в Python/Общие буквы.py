w = set()
o = []

for tt in range(3):
    g = input()
    p = set()
    for u in g:
        if u not in w:
            w.add(u)
        else:
            if u not in p:
                if u not in o:
                    o.append(u)
        p.add(u)
for u in o:
    print(u, end='')

