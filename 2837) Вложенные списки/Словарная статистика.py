p = []
a = input()
while a != '':
    line = []
    for u in a:
        col = 0
        for t in a:
            if t == u:
                col += 1
        line.append(col)
    p.append(line)
    a = input()
print(p)

