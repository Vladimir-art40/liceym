import sys

a = input()
b = input()
c = input()
if a == '3' or a == 'три':
    if b == '2' or b == 'два':
        if c == '1' or c == 'раз':
            print('ПУСК')
            sys.exit(0)
print('ОШИБКА')

