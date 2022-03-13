m = input()
out = dict()
while m != '':
    k = m.split()
    out[k[0]] = k[1:]
    m = input()

was = set()
m = input()
while m != '':
    was.add(m)
    m = input()
for elem, val in out.items():
    good = True
    for t in val:
        if t not in was:
            good = False
            break
    if good:
        print(elem)

