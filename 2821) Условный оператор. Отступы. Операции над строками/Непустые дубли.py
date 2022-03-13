import sys as Anna

a = [input() for i in range(2)]
if a[0] == '' or a[1] == '':
    print('Пусто!')
    Anna.exit(0)
print(min(a[0], a[1]) * 5)

