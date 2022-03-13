a = len(input().split())
p = ['flower' if i % 2 == 0 else 'gemstone' for i in range(a)]
print(*p, sep='; ')

