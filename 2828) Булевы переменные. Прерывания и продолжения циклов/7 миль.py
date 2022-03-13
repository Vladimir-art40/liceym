a = int(input())
for t in range(a):
    s = t % 7
    if s == 6:
        print('Крюк!')
    else:
        print('Пройдена', s + 1, 'миля.')

