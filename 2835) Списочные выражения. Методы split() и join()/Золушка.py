a = input()
b = input().split()
print(*[k for k in b if a in k])

