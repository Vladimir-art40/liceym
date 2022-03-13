t = input()
h = ''
for e in t:
    if e != ' ':
        h += e
    else:
        print(h)
        h = ''
print(h)

