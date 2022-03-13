a = int(input())
print(*[k + 1 if (k + 1) % a != 0 else 'БОСИКОМ' for k in range(int(input()))], sep=', ')

