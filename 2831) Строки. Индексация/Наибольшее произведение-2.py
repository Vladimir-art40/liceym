t = input()
k = int(input())
e = 0
for i in range(len(t) - (k - 1)):
    su = 1
    for h in range(k):
        su *= int(t[i + h])
    if su > e:
        e = su
print(e)

