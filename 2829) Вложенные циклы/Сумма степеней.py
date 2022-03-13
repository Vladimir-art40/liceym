a = int(input())
out = 0
for i in range(1, a + 1):
    f = 0
    for j in range(1, i + 1):
        if (j + i) % 2 == 0:
            f += j
    out += i ** f
print(out)

