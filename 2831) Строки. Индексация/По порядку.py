import sys


r = input()
f = 'A'
for g in r:
    if g >= f:
        f = g
    else:
        print(g)
        sys.exit(0)
print('(:_0_:)')

