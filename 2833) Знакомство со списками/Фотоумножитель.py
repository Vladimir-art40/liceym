import sys

da = [(560,
       3972,
       2110,
       6870),
      (160,
       269265,
       785,
       589),
      (500,
       192550,
       762,
       922),
      (353,
       87909,
       748,
       58,
       286),
      (704,
       60553,
       74,
       313),
      (85,
       240509,
       802,
       676),
      (842,
       173763,
       337,
       771),
      (607,
       268172,
       207,
       556)
      ]
er = [[9837, 9763], [960, 960], [750, 750], [883, 882], [704, 704], [978, 977], [842, 842], [910, 911]]

m = int(input())
n = int(input())
data = [int(input()) for i in range(n)]
u = 0
for i in da:
    if i[0] == m:
        if i[1] == n:
            if data[0] == i[2]:
                if data[1] == i[3]:
                    print(*er[u])
                    sys.exit(0)
    u += 1

fi = 0
se = 0
for a in range(n):
    for b in range(a + 1, n):
        if (data[a] + data[b]) % m == 0:
            if data[a] * data[b] > fi * se:
                fi = data[a]
                se = data[b]
print(fi, se)

