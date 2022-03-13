n = int(input())
m = int(input())
p = [[input() for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        bad = False
        if i > 0 and (p[i - 1][j][0] == p[i][j][0] or len(p[i - 1][j]) == len(p[i][j])):
            bad = True
        if i + 1 < n and (p[i + 1][j][0] == p[i][j][0] or len(p[i + 1][j]) == len(p[i][j])):
            bad = True
        if j > 0 and (p[i][j - 1][0] != p[i][j][0] and len(p[i][j - 1]) != len(p[i][j])):
            bad = True
        if j + 1 < m and (p[i][j + 1][0] != p[i][j][0] and len(p[i][j + 1]) != len(p[i][j])):
            bad = True
        if bad:
            print((i, j))


