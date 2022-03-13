m = int(input()) - 1
i = 1
while m > 0:
    r = len(str(i))
    e = int('9' + '0' * (r - 1))
    if m > e * r:
        m -= e * r
        i += e
    else:
        i += m // r
        break
print(i)

