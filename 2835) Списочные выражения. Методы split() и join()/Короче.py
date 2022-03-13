a = input()
print(a)
print(*[a[k:-k] for k in range(1, len(a) // 2 + len(a) % 2)], sep='\n')

