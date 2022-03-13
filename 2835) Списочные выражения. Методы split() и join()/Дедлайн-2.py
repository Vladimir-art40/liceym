a = int(input())
print(*[k - 2 for k in range(a + a % 2, 13, 2)])

