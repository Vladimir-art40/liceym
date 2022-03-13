m = int(input())
out = dict()
for _ in range(m):
    t = input().split()
    for p in range(0, len(t), 3):
        col = t[p] + ' ' + t[p + 1] + ' ' + t[p + 2]
        if col in out:
            out[col] += 1
        else:
            out[col] = 1
mx = 0
for t in out.values():
    mx = max(t, mx)

for elem, val in out.items():
    if val == mx:
        print(elem)
        

