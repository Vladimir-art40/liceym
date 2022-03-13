a = int(input())
print(*[k * k for k in range(a) if len(set(str(k))) == 1 and k % 10 == 1], sep=', ')

