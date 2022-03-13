n = int(input())
m = int(input())
for i1 in range(n):
    for i2 in range(n):
        i3 = n - i1 - i2
        if i3 >= 0:
            if i1 * 25 + i2 * 10 + i3 * 7 == m:
                print(i1, i2, i3)

