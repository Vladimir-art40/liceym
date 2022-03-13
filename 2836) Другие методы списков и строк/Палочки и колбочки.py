a = input()
b = int(input()) > 100
if b:
    a = a.replace('0000', '|||')
else:
    a = a.replace('|||', '00', 3)
a = a.replace('|0|', '|00|', 1)
print(a)

