a = input()
k = ''
for e in range(len(a)):
    if a[e] != '-':
        k += a[e]
    else:
        print(a[e + 1:] + '-' + k)

