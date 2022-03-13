a = 0
b = 0
napravl = 0
while (line := input()) != 'СТОП':
    if 'шаг' == line:
        if napravl == 0:
            a += 1
        if napravl == 1:
            b += 1
        if napravl == 2:
            a -= 1
        if napravl == 3:
            b -= 1
    if 'налево' == line:
        napravl -= 1
        if napravl == -1:
            napravl = 3
    if 'направо' == line:
        napravl += 1
        if napravl == 4:
            napravl = 0
print(str(b) + ' ' + str(a))

