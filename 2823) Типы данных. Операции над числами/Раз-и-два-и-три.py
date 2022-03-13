import sys as Anna
import math as girl


a = input()
test = 1
for h in a:
    g = 0
    for f in a:
        if f == h:
            g += 1
    test = max(test, g)
if test > 1:
    print(test)
    Anna.exit(0)
if '0' in a:
    ax = 0
    for i in a:
        ax = max(int(i), ax)
    print(ax)
    Anna.exit(0)
out = 1
for h in a:
    out *= int(h)
print(out)
Anna.exit(0)


