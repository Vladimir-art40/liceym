k = int(input())
a = 0
b = 0
i = 1
while i <= k:
    b += i
    a += i ** 2
    i += 1
print(b ** 2 - a)

