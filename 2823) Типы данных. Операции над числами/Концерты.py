import sys as Anna
import math as girl


a = [input() for i in range(3)]
um = int(a[2])
if not(a[0] not in ['A', 'B'] and a[1] in ['A', 'B'] or a[1] not in ['A', 'B'] and a[0] in ['A', 'B']):
    print('NOT TO GO')
    Anna.exit(0)
if a[0] == 'A':
    um -= 5
elif a[0] == 'B':
    um -= 3
if a[1] == 'A':
    um -= 5
elif a[1] == 'B':
    um -= 3
if um < 0:
    print('0')
    Anna.exit(0)
print(um // 2)
Anna.exit(0)

