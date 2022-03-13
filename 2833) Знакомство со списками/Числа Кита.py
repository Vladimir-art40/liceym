f = input()

num = len(f)
poz = num - 1
stepper = 0

out = []
for h in f:
    out.append(int(h))

while True:
    if out[poz] == int(f):
        for g in out:
            print(g, end=' ')
        break

    stepper += 1
    if stepper == 10000:
        print('NO')
        break

    new = 0
    for e in range(num):
        new += out[poz - e]
    out.append(new)

    poz += 1


