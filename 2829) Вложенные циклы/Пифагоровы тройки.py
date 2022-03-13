n = int(input())

for i1 in range(1, n):
    for i2 in range(1, i1):
        if i1 ** 2 + i2 ** 2 > n:
            continue
        if i1 != 1 and i2 != 1 and i1 % i2 == 0 or i2 % 2 == 1 and i1 % 2 == 1 or i2 % 2 == 0 and i1 % 2 == 0:
            continue
        f = False
        for i in range(2, i2 + 1):
            if i1 % i == 0 and i2 % i == 0:
                f = True
                break
        if f:
            continue
        print(i1 ** 2 - i2 ** 2, 2 * i1 * i2, i1 ** 2 + i2 ** 2)

