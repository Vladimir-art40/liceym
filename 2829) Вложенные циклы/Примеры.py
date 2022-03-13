a = int(input())
b = int(input())
c = int(input())
d = (b - a) // c + 1
for i in range(d):
    for j in range(d):
        print(a + i * c, '+', a + j * c, '=', a + i * c + a + j * c, end='\t')
    print()

