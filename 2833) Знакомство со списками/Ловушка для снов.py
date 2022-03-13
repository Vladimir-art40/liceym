h = []
e = input()
while e != '':
    h.append(e)
    e = input()

fr = int(input())
to = int(input())
g = ''
for y in range(fr, to + 1):
    if len(h[y - 1]) > len(g):
        g = h[y - 1]
print(g)

