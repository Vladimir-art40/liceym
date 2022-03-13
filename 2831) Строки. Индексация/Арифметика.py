r = input()
g = int(r[0])
for t in range(1, len(r), 2):
    p = r[t]
    if r[t] == '+':
        g += int(r[t + 1])
    else:
        g -= int(r[t + 1])
print(g)

