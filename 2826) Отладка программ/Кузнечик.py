a = 0
n = int(input())
m = int(input())
while (f := int(input())) != 0:
    if f == -1:
        a -= m
    elif f == 1:
        a += n
print(a)

