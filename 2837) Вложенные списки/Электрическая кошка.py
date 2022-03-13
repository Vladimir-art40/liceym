m = int(input())
n = int(input())
p = [[0 for _ in range(m)] for _ in range(n)]
a, b = int(input()), int(input())
power = int(input())
rad = 0
while True:
    for i in range(max(a - rad, 0), min(a + rad + 1, len(p[0]))):
        if b - rad >= 0:
            p[b - rad][i] = power
        if b + rad < n:
            p[b + rad][i] = power
    for j in range(max(b - rad, 0), min(b + rad + 1, len(p))):
        if a - rad >= 0:
            p[j][a - rad] = power
        if a + rad < m:
            p[j][a + rad] = power

    rad += 1
    power = int(power ** 0.5)
    if power == 1:
        break

for line in p:
    print(*line, sep='\t')

