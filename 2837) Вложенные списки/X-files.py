n = int(input())
p = [input().split() for _ in range(n)]
m = len(p[0])
for i in range(1, n - 1):
    line = []
    for j in range(1, m - 1):
        word = p[i][j] + p[i - 1][j - 1] + p[i - 1][j + 1] \
               + p[i + 1][j - 1] + p[i + 1][j + 1]
        line.append(word)
    print(*line)
    

