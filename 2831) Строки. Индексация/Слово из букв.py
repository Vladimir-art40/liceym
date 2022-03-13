import sys


p = int(input())
e = ''
for t in range(p):
    w = input()
    if len(w) < t + 1:
        print('None')
        sys.exit(0)
    else:
        e += w[-(t + 1)]
print(e)

