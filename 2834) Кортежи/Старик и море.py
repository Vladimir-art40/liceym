n = int(input())
k = 10
p = ''
for i in range(n):
    j = input()
    r = int(j[-1])
    if r > k:
        print((i, p))
    k = r
    p = j[:-2]


