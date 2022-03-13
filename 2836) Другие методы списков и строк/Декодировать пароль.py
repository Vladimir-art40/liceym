b = input()

a = ''
last = '-'
num = 0
for k in b:
    if k == '%' and last == '-':
        continue
    if k != '%':
        a += k
        last = k
        num = 0
    if k == '%':
        num += 1
        if num > 1:
            a += last + '%'
            num = -1000000
ignore = 0
for i in range(len(a) - 1):
    if ignore > 0:
        ignore -= 1
        continue
    if a[i] == a[i + 1]:
        k = 2
        copir = a[i]
        while i + k < len(a) and a[i + k] == copir:
            k += 1
        print(copir, end='')
        ignore = k - 1

