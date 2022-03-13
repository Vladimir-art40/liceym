a = int(input())


def Factor(n):
    Ans = []
    asd = 2
    while asd * asd <= n:
        if n % asd == 0:
            Ans.append(asd)
            n //= asd
        else:
            asd += 1
    if n > 1:
        Ans.append(n)
    return Ans


f = Factor(a)
print(a, '=', end=' ')
print(*f, sep=' * ')

