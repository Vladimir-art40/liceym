n = int(input())
p = [[int(k) for k in input().split()] for _ in range(n)]
su = 0
m = len(p[0])
for i in range(m):
    su += p[0][i] + p[n - 1][i]
for i in range(n):
    su += p[i][0] + p[i][m - 1]
su -= p[0][0]
su -= p[0][m - 1]
su -= p[n - 1][0]
su -= p[n - 1][m - 1]
p[n // 2][m // 2] = su
for line in p:
    print(*line, sep='\t')

