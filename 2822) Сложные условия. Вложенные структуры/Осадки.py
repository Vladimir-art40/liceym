import sys

data = sys.stdin.readline()
if data.__contains__('дожд') or data.__contains__('Дожд'):
    print('Возьми зонт!')
    sys.exit(0)
if data.__contains__('осадки') or data.__contains__('Осадки'):
    print('Возьми зонт!')
    sys.exit(0)
print("Зонт не нужен.")

