a = int(input())
b = a
c = 1
while (k := input()) != 'КОНЕЦ':
    if 'доска' in k or 'дощечка' in k:
        print('Прибили', c, 'дощечку.')
        c += 1
        b -= 1
        if b == 0:
            break
if b == 0:
    print('ГОТОВО')
else:
    print('МАЛОВАТО')

