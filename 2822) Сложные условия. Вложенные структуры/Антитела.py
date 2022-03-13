na = input().split()
nb = input().split()
nc = input().split()
f = [na, nb, nc]
f = sorted(f)
na = f[0]
nb = f[1]
nc = f[2]
out = ''
if na[1] == '0':
    out += na[0] + ' 0, '
if nb[1] == '0':
    out += nb[0] + ' 0, '
if nc[1] == '0':
    out += nc[0] + ' 0, '
if len(out) > 0:
    print(out[:-2])

