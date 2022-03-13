a = int(input())
b = 1
c = False
g = False
while (n := int(input())) != 0:
    if n > 20:
        c = True
    if a - n > 0:
        a -= n
        b += 1
    else:
        print('Время заполнения ' + str(b) + ' секунд.')
        g = True
        break
if not g:
    print('Ведро не полное.')
if c:
    print('Град был!')
else:
    print('Града не было.')

