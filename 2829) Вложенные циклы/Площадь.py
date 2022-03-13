a = int(input())
for i in range(1, int(a ** 0.5 + 1)):
    if a % i == 0:
        print(i, ' ', a // i)

