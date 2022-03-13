a = int(input())
out = 0
for i in range(1, a + 1):
    if a % i == 0:
        out += i
print(out)

