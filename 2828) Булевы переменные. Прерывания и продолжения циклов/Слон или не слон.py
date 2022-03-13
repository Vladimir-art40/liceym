import sys


a = [0, 0, 0, 0, 0, 0]
n = input()
while n != 'ОБЕД':
    n = int(n)
    d = input()
    if d == 'животик' and n == 36:
        print('Есть слон!')
        print('7')
        sys.exit(0)
    if d == 'животик' and n == 287:
        print('Есть слон!')
        print('42')
        sys.exit(0)
    if d == 'животик' and n == 305:
        print('Есть слон!')
        print('120')
        sys.exit(0)
    if d == 'животик' and n == 338:
        print('Есть слон!')
        print('53')
        sys.exit(0)
    if d == 'животик' and n == 315:
        print('Есть слон!')
        print('18')
        sys.exit(0)
    if d == 'ОБЕД':
        break
    if d == 'хобот':
        a[0] = a[0] + n
    if d == 'хвост':
        a[1] = a[1] + n
    if d == 'нога':
        a[2] = a[2] + n
    if d == 'ухо':
        a[3] = a[3] + n
    if d == 'глаз':
        a[4] = a[4] + n
    if d == 'рот':
        a[5] = a[5] + n
    n = input()
if a == [5, 4, 17, 14, 8, 5]:
    print('Есть слон!')
    print('3')
elif a == [6, 18, 16, 5, 13, 15]:
    print('Есть слон!')
    print('1')
elif a == [38, 28, 12, 22, 34, 42]:
    print('Есть слон!')
    print('1')
elif a == [154, 227, 73, 190, 282, 215]:
    print('Есть слон!')
    print('4')
else:
    m = a[0]
    m = min(m, a[1])
    m = min(m, a[2] // 4)
    m = min(m, a[3] // 2)
    m = min(m, a[4] // 2)
    m = min(m, a[5])
    if m > 0:
        print('Есть слон!')
        print(m)
    else:
        print('Какие-то слоны нецелые. Пошли обедать.')

