a = 0
b = 0
c = 0
k = int(input())
g = int(input())
while (x1 := input()) != 'END':
    x1 = int(x1)
    y1 = int(input())
    y2 = x1 * k + g
    if y2 > y1:
        b += 1
    elif y2 < y1:
        a += 1
    else:
        c += 1

if a > 0:
    print('Выше прямой: ' + str(a))
if b > 0:
    print('Ниже прямой: ' + str(b))
if c > 0:
    print('На прямой: ' + str(c))

