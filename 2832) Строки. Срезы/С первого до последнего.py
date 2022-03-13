def find(st, ch):
    for t in range(len(st)):
        if st[t] == ch:
            return t
    return -1


a = input()
b = input()
q1 = find(b, a)
q2 = len(b) - 1 - find(b[::-1], a)
if q1 == -1:
    print(b)
elif q1 == q2:
    print(b[q1 + 1:])
else:
    print(b[q1 + 1:q2])

