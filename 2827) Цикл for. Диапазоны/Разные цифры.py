a = int(input())
b = int(input())


def diff(asd):
    for g in str(asd):
        h = 0
        for j in str(asd):
            if j == g:
                h += 1
        if h > 1:
            return False
    return True


for i in range(a, b + 1):
    if diff(i):
        print(i)

