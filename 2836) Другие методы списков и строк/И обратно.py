a, b = input().split(), input().split()
print(sum([int(r) for r in a][min(int(b[0]), int(b[1])):max(int(b[0]), int(b[1]))]))

