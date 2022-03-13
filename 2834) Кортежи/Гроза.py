n = int(input())
s = []
for i in range(n):
    s.append((int(input()), float(input())))

while len(s) > 0:
    u = max(s)
    s.remove(u)
    print(u)

