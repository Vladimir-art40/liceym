a = input()
if len(a) % 2 == 0:
    for t in range(len(a) // 2 - 1, -1, -1):
        print(' ' * t + a[t] + ' ' * (len(a) - 2 - t * 2) + a[-(t + 1)])
else:
    print(' ' * (len(a) // 2) + a[len(a) // 2])
    for t in range(len(a) // 2 - 1, -1, -1):
        print(' ' * t + a[t] + ' ' * (len(a) - 2 - t * 2) + a[-(t + 1)])

