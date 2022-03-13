h = ''
e = input()
while e != '</html>':
    h += e + ' '
    e = input()

out_all = []
for t in range(len(h)):
    if h[t:t + 3] == '<p>':
        out = ''
        j = t + 2
        while h[j:j + 4] != '</p>':
            j += 1
            out += h[j]
        out_all.append(out[:-1])
out_all.reverse()
for g in out_all:
    print(g)

