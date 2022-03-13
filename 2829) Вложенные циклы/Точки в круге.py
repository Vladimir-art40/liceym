x = int(input())
y = int(input())
r = int(input())
o = 0
for i in range(1, r):
    o += int((r ** 2 - i ** 2) ** 0.5) + 1
print(o * 4 + 5)


