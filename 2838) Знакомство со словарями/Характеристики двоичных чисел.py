m = map(int, input().split())
out = []
for i in m:
    o = dict()
    o['digits'] = len(bin(i)[2:])
    o['units'] = len([k for k in bin(i)[2:] if k == '1'])
    o['zeros'] = len([k for k in bin(i)[2:] if k == '0'])
    out.append(o)
print(out)


