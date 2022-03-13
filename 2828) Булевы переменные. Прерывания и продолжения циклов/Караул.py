while (n := int(input())) != 0:
    a1 = n % 3 == 0
    a2 = n % 7 == 0
    if a1 and a2:
        print('Караул!')
        break
    elif a1:
        print('несчастливое')
    elif a2:
        print('опасное')
    else:
        print(n)

