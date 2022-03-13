a = input()
b = input()

if 'e' in a.lower():
    a1 = float(a.split('e')[0]) * (10 ** int(a.split('e')[1]))
else:
    a1 = int(a.replace('_', ''))
if 'e' in b.lower():
    a2 = float(b.split('e')[0]) * (10 ** int(b.split('e')[1]))
else:
    a2 = int(b.replace('_', ''))
a3 = a2 * 60 * 60 * 24 * 365
print(a1 / a3)

