a = ''
while (line := input()) != '':
    if len(line) > 99:
        print(a)
    elif len(line) % 2 == 0:
        print(line * 2)
    elif len(line) % 3 == 0:
        print(line * 3)
    else:
        print(line)
    a = line

