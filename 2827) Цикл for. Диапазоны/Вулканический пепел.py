a = int(input())
b = int(input())
print(a, end=' ')
for u in range(10000000000):
    a -= b
    print(a, end=" ")
    if a - b <= 0:
        break
print(0)

