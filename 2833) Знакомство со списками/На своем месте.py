a = int(input())
k = []
for t in range(a):
    k.append(input())
d = input()
o = False
for t in range(len(k)):
    if d < k[t]:
        print(t)
        o = True
        break
if not o:
    print(a)

