a = input()
j = 0
k = 0
for i in range(len(a)):
    if i % 2 == 0:
        print(a[k], end='')
        k += 1
    else:
        print(a[len(a) // 2 + len(a) % 2 + j], end='')
        j += 1

