m = []
a = int(input())
for i in range(a):
    ln = input().replace(',', ' ').split()
    m.append(ln)

e = 0
for i in range(a):
    for j in range(len(m[i])):
        if i == j or i == len(m[i]) - j - 1:
            e += int(m[i][len(m[i]) - j - 1])
            if i == (a - 1) / 2:
                e += int(m[i][len(m[i]) - j - 1])
            print(m[i][len(m[i]) - j - 1], end=' ')
        else:
            print(m[i][j], end=' ')
    print()
print(e)

