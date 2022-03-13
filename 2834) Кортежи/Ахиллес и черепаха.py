a = int(input())
s = []
while a != 0:
    s.append(a)
    a = int(input())

while len(s) > 0:
    u = max(s)
    s.remove(u)
    if len(s) > 0:
        print(u, end='->')
    else:
        print(u)

