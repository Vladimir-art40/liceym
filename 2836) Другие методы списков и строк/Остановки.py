a, b = input().split(), input().split()
print(sum([int(r) for r in a][int(b[0]):int(b[1])]))

