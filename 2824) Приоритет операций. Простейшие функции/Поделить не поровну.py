i = int(input())
a1 = i % 10
i = i // 10
a2 = i % 10
i = i // 10
a3 = i % 10
i = i // 10
a4 = i % 10
i = i // 10

if a1 > a2:
    a1, a2 = a2, a1
if a2 > a3:
    a2, a3 = a3, a2
if a3 > a4:
    a3, a4 = a4, a3
if a1 > a2:
    a1, a2 = a2, a1
if a2 > a3:
    a2, a3 = a3, a2
if a3 > a4:
    a3, a4 = a4, a3
if a1 > a2:
    a1, a2 = a2, a1
if a2 > a3:
    a2, a3 = a3, a2
if a3 > a4:
    a3, a4 = a4, a3
if a1 > a2:
    a1, a2 = a2, a1
if a2 > a3:
    a2, a3 = a3, a2
if a3 > a4:
    a3, a4 = a4, a3

if a1 != 0:
    print(str(a1) + str(a2) + ' ' + str(a4) + str(a3))
elif a2 != 0:
    print(str(a2) + str(a1) + ' ' + str(a4) + str(a3))
else:
    print(str(a3) + str(a1) + ' ' + str(a4) + str(a2))


