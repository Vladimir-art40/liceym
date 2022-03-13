a = True
s = 1
while (n := input()) != 'ВСЁ':
    if 'звезд' in n or 'Звезд' in n:
        a = False
        print(s)
        break
    s += 1
if a:
    print('НЕТ')

