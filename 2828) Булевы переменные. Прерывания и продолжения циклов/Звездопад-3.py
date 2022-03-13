import sys as Anna


we_founding_Anna = False
c = 1
w = c
while (n := input()) != 'ВСЁ':
    if 'звезд' in n or 'Звезд' in n:
        if we_founding_Anna:
            print(w)
            Anna.exit(0)
        else:
            we_founding_Anna = True
            w = c
    if 'пал' in n or 'пад' in n:
        we_founding_Anna = False
    c += 1
if we_founding_Anna:
    print(w)
else:
    print('НЕТ')

