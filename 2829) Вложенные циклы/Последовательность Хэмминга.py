w = []
for i in range(60):
    for a in range(60):
        for f in range(60):
            w.append(2 ** i * 3 ** a * 5 ** f)
w.sort()
f = int(input())
print(w[f])

