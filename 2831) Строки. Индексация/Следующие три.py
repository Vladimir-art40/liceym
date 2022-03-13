r = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
q = int(input()) - 1
q %= 26
print(r[q] + r[q + 1] + r[q + 2] + r[q + 3])

