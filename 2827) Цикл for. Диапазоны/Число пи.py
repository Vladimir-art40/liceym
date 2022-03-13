num = int(input())
a = 4
s = 0
for i in range(0, num):
    s += int((-1)**i) / (2 * i + 1)
print(a * s)

