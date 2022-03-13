import sys


a = input()
b = input()
if a == b:
    print(0)
    sys.exit(0)
for i in range(1, len(a)):
    r = a[-i:] + a[0:-i]
    if r == b:
        print(i)
        sys.exit(0)
print('NO')

