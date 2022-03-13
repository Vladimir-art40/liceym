a = int(input())
a1 = 1
a2 = 1
c = 2
while a2 < a:
    a2, a1, c = a2 + a1, a2, c + 1
if a2 == a:
    print(c)
else:
    print('НЕТ')

