import math
import sys


n = float(input())
if n == 0:
    print('INFINITELY LARGE')
    sys.exit(0)
out = 1 / n
if abs(out) < 10**-9:
    print('INFINITELY SMALL')
elif abs(out) > 10**9:
    print('INFINITELY LARGE')
else:
    print(out)

