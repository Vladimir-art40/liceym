h = []
e = int(input())
while e != 0:
    h.append(e)
    e = int(input())
out = []
for i in h:
    if i % len(h) == 0:
        out.append(i)
print(out)

