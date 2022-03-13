a = input()
b = input()
c = input()
d = input()
out = 'В букете есть '
if a in d:
    out += a + ', '
if b in d:
    out += b + ', '
if c in d:
    out += c + ', '
if out != 'В букете есть ':
    print(out[:-2] + '.')
else:
    print('Таких цветов в букете нет.')


