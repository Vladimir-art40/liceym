a = int(input())
b = int(input())
now = 0
rev = 1
grow = True
for i in range(b):
    t = input()
    if grow:
        if len(t) + now < a:
            print(' ' * now + t)
            now += 1
        else:
            grow = False
            now = a - len(t)
            print(' ' * now + t)
            rev = 1
    else:
        if a - rev > len(t):
            print(' ' * (a - len(t) - rev) + t)
            rev += 1
        else:
            grow = True
            print(t)
            now = 1

