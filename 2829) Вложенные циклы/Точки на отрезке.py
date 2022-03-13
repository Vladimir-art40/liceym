x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
o = 1
x2 = abs(x1 - x)
y2 = abs(y1 - y)
d = y2 / x2
for g in range(x2):
    if g * d == int(g * d):
        o += 1
print(o)

