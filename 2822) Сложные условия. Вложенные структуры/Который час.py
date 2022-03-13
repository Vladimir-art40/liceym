import sys


a = ['4', '5', '6', '7', '8', '9', '10']
b = ['11', '12', '13', '14', '15', '16', '17']
c = ['18', '19', '20', '21', '22']
d = ['23', '0', '1', '2', '3']
i = input()
if i in a:
    print('Утро')
    sys.exit(0)
if i in b:
    print('День')
    sys.exit(0)
if i in c:
    print('Вечер')
    sys.exit(0)
if i in d:
    print('Ночь')
    sys.exit(0)
print('Ошибка')


