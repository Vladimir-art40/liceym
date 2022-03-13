import sys


a = sys.stdin.readline()
b = sys.stdin.readline()
c = sys.stdin.readline()
if a.__contains__('три'):
    if b.__contains__('два'):
        if c.__contains__('раз') or c.__contains__('один'):
            print('ПУСК')
            sys.exit(0)
print('ОШИБКА')

