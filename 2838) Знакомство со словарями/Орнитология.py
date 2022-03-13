m = input()
out = dict()
while m != '':
    k, f = m.split(': ')
    f = int(f)
    if k in out:
        out[k] += f
    else:
        out[k] = f
    m = input()
print(out)

