a = input()
n = int(input())
if a == 'фартинг':
    pha1 = n % 4
    p1 = n // 4
    sh1 = p1 // 12
    pht1 = sh1 // 20
    p1 = p1 % 12
    sh1 = sh1 % 20

    if pht1 != 0:
        print('Фунтов:', pht1)
    if sh1 != 0:
        print('Шиллингов:', sh1)
    if p1 != 0:
        print('Пенсов:', p1)
    if pha1 != 0:
        print('Фартингов:', pha1)
else:
    sh1 = n // 12
    pht1 = sh1 // 20
    p1 = n % 12
    sh1 = sh1 % 20
    if pht1 != 0:
        print('Фунтов:', pht1)
    if sh1 != 0:
        print('Шиллингов:', sh1)
    if p1 != 0:
        print('Пенсов:', p1)

