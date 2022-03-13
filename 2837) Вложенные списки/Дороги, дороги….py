data = []
num = []
a = input()
while a != '':
    data.append((a[0], a[1]))
    if a[0] not in num:
        num.append(a[0])
    if a[1] not in num:
        num.append(a[1])
    a = input()
num.sort()
p = [[0 for _ in range(len(num))] for _ in range(len(num))]
for pair in data:
    y = num.index(pair[0])
    x = num.index(pair[1])
    p[y][x] = 1
print(' ', *num)
for i in range(len(p)):
    print(num[i], *p[i])
    

