m = input()
da = [145, 155, 335, 2165, 100000000]
ne = ['Cenozoic', 'Mesozoic', 'Paleozoic', 'Proterozoic', 'Archaea']
while m != '':
    n = int(m) / 1000
    poz = -1
    while n > da[poz + 1]:
        poz += 1
        n -= da[poz]
    print(ne[poz + 1])
    m = input()

