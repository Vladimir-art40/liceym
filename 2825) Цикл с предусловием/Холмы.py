a = int(input())
b = int(input())
out = 0
while (c := int(input())) != -1:
    if a < b > c:
        out += 1
    a, b = b, c
print(out)

