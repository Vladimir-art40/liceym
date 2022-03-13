a = int(input())
b = int(input())
c = int(input())
for i in range(1, c + 1):
    a -= b
    if a >= 0:
        print('Чашечка', i, 'полная. В чайнике осталось', str(a) + '.')
    elif a > -b:
        print('Чашечка', i, 'неполная. В чайнике осталось 0.')
    else:
        print('Чашечка', i, 'пустая. В чайнике осталось 0.')

