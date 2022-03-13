import sys

a = input()
b = input()
c = input()
while len(a) < len(b) and len(a) < len(c):
    print(a)
    sys.exit(0)
while len(b) < len(a) and len(b) < len(c):
    print(b)
    sys.exit(0)
while len(c) < len(b) and len(c) < len(a):
    print(c)
    sys.exit(0)
while len(c) == len(b) and len(c) < len(a):
    print(min(b, c))
    sys.exit(0)
while len(a) == len(b) and len(a) < len(c):
    print(min(b, a))
    sys.exit(0)
while len(c) == len(a) and len(c) < len(b):
    print(min(a, c))
    sys.exit(0)
print(min(a, b, c))

