n = int(input())
was = set()
q = set()
o = 0
for t in range(n):
    m = int(input())
    for g in range(m):
        w = input()
        if w in was:
            o += 1
            q.add(w)
        else:
            was.add(w)
print(len(q), len(q) + o)

