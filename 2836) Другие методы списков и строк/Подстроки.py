f = input()

was = set()
for l in range(len(f) - 1):
    for r in range(l + 1, len(f)):
        st = f[l:r]
        if st in was:
            continue
        was.add(st)
        p = 0
        for t in range(len(f) - len(st) + 1):
            if f[t:].startswith(st):
                p += 1
        if p == 1:
            continue
        print(st + ': ' + str(p))

