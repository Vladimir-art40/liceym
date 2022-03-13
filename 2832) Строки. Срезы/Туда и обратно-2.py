b = input()
a = ''
for p in b:
    if p != ' ':
        a += p
print(a == a[::-1])

