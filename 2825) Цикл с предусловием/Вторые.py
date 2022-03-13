a = int(input())
b = int(input())
if b > a:
    a, b = b, a
while -1000 < (i := int(input())) < 1000:
    if i >= a:
        a, b = i, a
    elif i >= b:
        b = i
print(b)

