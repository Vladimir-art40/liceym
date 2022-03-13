er = input()
k = int(input())
hmax = 0
o = set()
for t in range(k):
    r = set(input())
    h = len(r)
    if er in r:
        h -= 1
    if hmax < h:
        hmax = h
        o = r
if hmax == 0:
    print(-1)
for t in o:
    if t != er:
        print(t, end='')

