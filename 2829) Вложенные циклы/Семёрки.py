o = 0
while (f := int(input())) > 0:
    while f > 0:
        if f % 8 == 7:
            o += 1
        f //= 8
print(o)

