a1 = 0
a2 = 0
d = ''
while (n := input()) != '':
    if n == 'добрый':
        a1 += 1
    if n == 'злой':
        a2 += 1
    if n == 'Какой подарок?':
        if a2 > a1 and d == 'злой':
            print('золотой')
        elif a1 > a2 and d == 'добрый':
            print('серебряный шиллинг')
        else:
            print('Ах, не знаю!')
            break
        a1 = 0
        a2 = 0
    d = n

