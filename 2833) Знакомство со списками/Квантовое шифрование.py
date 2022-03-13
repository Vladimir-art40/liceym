n = int(input())
m = int(input())
messages = [input() for i in range(n)]
codes = [input() for i in range(m)]
was = set()
out = []
for step in codes:
    chet = 0
    for j in range(len(step)):
        if step[j].isdigit():
            chet *= 10
            chet += int(step[j])

    check = ''
    for t in range(len(step)):
        if (t - chet + 1) % chet == 0:
            check += step[t]
    if check in messages:
        out.append(check)

for t in out:
    if t not in was:
        print(t)
        was.add(t)

if len(out) == 0:
    print('NO')

