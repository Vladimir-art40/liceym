a = 0
b = input()
while (c := input()) != '':
    if len(c) < len(b):
        break
    a += 1
    b = c
if a % 2 != 0:
    print('Первый')
else:
    print("Второй")

