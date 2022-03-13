n = int(input())
y = []
for t in range(n):
    y.append(input())

while len(y) > 0:
    k = y[0]
    kn = 0
    for i in y:
        if i == k:
            kn += 1

    for t in range(kn):
        y.remove(k)
        
    print((kn, k))

