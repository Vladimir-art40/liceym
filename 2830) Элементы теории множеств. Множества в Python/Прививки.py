a = int(input())
ad = []
for p in range(a):
    ad.append(input())

e = set()

b = int(input())
for p in range(b):
    t = input()
    if t in ad and t not in e:
        print(t)
        e.add(t)

