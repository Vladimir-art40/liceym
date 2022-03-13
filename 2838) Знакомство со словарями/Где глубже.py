out = dict()
a = input()
while a != '':
    t = a.split()
    if t[0] in out:
        a, b = out[t[0]]
        out[t[0]] = (min(a, int(t[1])), max(b, int(t[1])))
    else:
        out[t[0]] = (int(t[1]), int(t[1]))
    a = input()
print(out)

