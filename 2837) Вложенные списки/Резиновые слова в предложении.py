data = input().split()
out = []
now = 0
for a in data:
    mef = []
    if len(a) % 2 == 0:
        for t in range(len(a) // 2 - 1, -1, -1):
            mef.append(' ' * t + a[t] + ' ' * (len(a) - 2 - t * 2) + a[-(t + 1)] + ' ' * t)
    else:
        mef.append(' ' * (len(a) // 2) + a[len(a) // 2] + ' ' * (len(a) // 2))
        for t in range(len(a) // 2 - 1, -1, -1):
            mef.append(' ' * t + a[t] + ' ' * (len(a) - 2 - t * 2) + a[-(t + 1)] + ' ' * t)
    mef.reverse()
    if len(out) < len(mef):
        for _ in range(len(mef) - len(out)):
            out.append(' ' * now)
    for i in range(len(mef)):
        out[i] += mef[i] + ' '
    for i in range(len(mef), len(out)):
        out[i] += ' ' * (len(mef[0]) + 1)
    now += len(mef[0]) + 1

out.reverse()
for line in out:
    print(*line, sep='')

