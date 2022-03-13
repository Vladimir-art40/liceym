out = dict()
a = input()
while not a.isdecimal():
    t = a.split(': ')
    if t[0] in out:
        out[t[0]] += int(t[1])
    else:
        out[t[0]] = int(t[1])
    a = input()
n = int(a)
prod = {'Сладкоежка': ['банан', 'молоко', 'мороженое'],
        'Клубнично-банановый': ['клубника', 'банан', 'молоко', 'мороженое'],
        'Клубничный': ['клубника', 'молоко', 'мороженое'],
        'Хушаф': ['молоко', 'финики'],
        'Банановый': ['молоко', 'финики', 'банан'],
        }
for i in range(n):
    name = input()
    can = True
    for e in prod[name]:
        if out[e] == 0:
            can = False
    if can:
        print(f'Пожалуйста, ваш {name}. Приятного аппетита!')
        for e in prod[name]:
            out[e] -= 1
    else:
        print('Извините, не можем выполнить заказ.')

