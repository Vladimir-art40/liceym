n = int(input())
p = []
for h in range(n):
    p.append(input())

m = int(input())
for h in range(m):
    k = input()
    if k in p:
        print('Вот твой подарок,', k + '!')
        p.remove(k)
    else:
        print(k + ', всем по одному подарку!')



