a = input()
t = 0
out = ''
for h in a:
    if h == '[':
        t += 1
    elif h == ']':
        t -= 1
    else:
        if t == 0:
            out += h
print(out)

