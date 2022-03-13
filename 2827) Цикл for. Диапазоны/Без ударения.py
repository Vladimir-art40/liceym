a = input()
b = 'аяоёэеуюыи'
o = 0
n = 0
for j in a:
    if j in b:
        o += 1
word = False
la = ' '
for j in a:
    if j != ' ' and la == ' ':
        word = True
    if word:
        if j in b:
            n += 1
            word = False
    if j == ' ':
        word = False
    la = j
print(o - n)

