a = input()
b = input()
c = input()
d = [a, b, c]
e = max(d)
f = min(d)
print(f)
print(e)
if a != e and a != f:
    print(len(a))
elif b != e and b != f:
    print(len(b))
else:
    print(len(c))

