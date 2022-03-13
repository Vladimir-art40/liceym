n = int(input())
h = []
su = 0
for fdkg in range(n):
    e = int(input())
    su += e
    h.append(e)
out = []
out_sum = 0
for i in h:
    if i % 2 == su % 2:
        out.append(i)
    else:
        out_sum += i
print(out_sum, out)

