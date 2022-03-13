p = set()
swge = int(input())
for t in range(swge):
    e = input()
    if e in p:
        print('ДА')
    else:
        print('НЕТ')
        p.add(e)

