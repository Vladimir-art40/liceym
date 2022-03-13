a = input()
b = input()
if a == b == 'Быть' or a == b == 'Не быть':
    print('Выбор сделан!')
elif (a == 'Быть' and b == 'Не быть') or (b == 'Быть' and a == 'Не быть'):
    print('Вот в чём вопрос!')
else:
    print('Определитесь!')

