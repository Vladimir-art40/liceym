n = input()
s = []
while n != 'разбитое корыто':
    s.append(n)
    n = input()

while len(s) > 0:
    u = min(s, key=len)
    s.remove(u)
    print(u)

