a = int(input())
was = False
xam = 0
for t in range(a):
    m = int(input())
    ma = 0
    for g in range(m):
        ma = max(ma, int(input()))
    if ma <= 60:
        xam = max(ma, xam)
    else:
        was = True
print(xam)
if was:
    print('ДА')
else:
    print('НЕТ')


