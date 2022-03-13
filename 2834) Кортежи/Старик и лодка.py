t = int(input())
for i in range(t):
    j = input()
    for e in range(1, len(j)):
        if j[e] < j[e - 1]:
            print((i, e))


