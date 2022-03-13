n, m = int(input()), int(input())
n = oct(n)[2:]
m = oct(m)[2:]
p = []
line = ['']
while n != m:
    k = int(n, 8) + 1
    line.append(n)
    n = oct(k)[2:]
line.append(n)
p.append(line)
for ln in range(1, len(line)):
    new = [line[ln]]
    for i in range(1, len(line)):
        nw = oct(int(str(line[i]), 8) * int(str(line[ln]), 8))[2:]
        new.append(nw)
    p.append(new)

for t in p:
    print(*t, sep='\t')

a, b = int(input()), int(input())
print(p[a + 1][b + 1])

