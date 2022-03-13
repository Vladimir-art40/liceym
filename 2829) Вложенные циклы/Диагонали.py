x = input()
y = int(input())
c = y // 2
if y % 2 != 0:
    for i in range(c):
        print(' ' * (i * 2), x, ' ' * (3 + 4 * (c - 1 - i)), x, ' ' * i * 2, sep='')
    print(' ' * (y - 1), x, ' ' * (y - 1), sep='')
    for h in range(c):
        i = c - h - 1
        print(' ' * (i * 2), x, ' ' * (3 + 4 * (c - 1 - i)), x, ' ' * i * 2, sep='')
else:
    c = c - 1
    for i in range(c):
        print(' ' * (i * 2), x, ' ' * (5 + 4 * (c - 1 - i)), x, ' ' * i * 2, sep='')
    print('  ' * c, x, ' ', x, '  ' * c, sep='')
    print('  ' * c, x, ' ', x, '  ' * c, sep='')
    for h in range(c):
        i = c - h - 1
        print(' ' * (i * 2), x, ' ' * (5 + 4 * (c - 1 - i)), x, ' ' * i * 2, sep='')

