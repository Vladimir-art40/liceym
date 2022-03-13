def ki(f, r):
    for t in range(len(r)):
        if r[t] == f:
            return t + 1


a = input()
ab = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
ac = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
e = set()
for i in a:
    if i in e:
        continue
    e.add(i)
    if i in ab:
        print((i, ki(i, ab)))
    if i in ac:
        print((i, ki(i, ac)))

