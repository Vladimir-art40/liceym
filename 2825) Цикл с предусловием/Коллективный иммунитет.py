a = 0
b = 0
while (line := input()) != "":
    if line == 'да':
        a += 1
    elif line == 'нет':
        b += 1
c = 100.0 * a / (a + b)
if c >= 80:
    print('Достигли')
else:
    print('Пока нет')

