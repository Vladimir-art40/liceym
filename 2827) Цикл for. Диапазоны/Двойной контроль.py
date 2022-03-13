a = input()
b = input()
g = 1
for i in range(0, len(a)):
    c = len(a) - i
    if len(a) % c == 0 and len(b) % c == 0:
        g = c
        break
e = ''
reg1 = 0
reg2 = 0
for t in b:
    if reg1 % g == 0:
        e += t
    reg1 += 1
for t in a:
    if reg2 % g == 0:
        e += t
    reg2 += 1
print(e)

