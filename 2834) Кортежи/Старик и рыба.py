n = input()
s = []
while n != '':
    s.append(n)
    n = input()

while len(s) > 0:
    u1 = min(s, key=len)
    u2 = min(s)
    s.remove(u1)
    if u1 != u2:
        print(u2, u1)
        break
if len(s) == 0:
    print('YES')

