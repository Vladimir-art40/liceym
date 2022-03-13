a = True
while (n := input()) != 'ВСЁ':
    if 'звезд' in n or 'Звезд' in n:
        a = False
        print('Загадывай!')
        break
if a:
    print('НЕТ')
    

