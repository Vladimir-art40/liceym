m = []
a = input()
while a != '':
    ln = a.replace(':', ' ').split()
    m.append(ln)
    a = input()

n = int(input())
for i in m:
    for j in i:
        if int(j) < n:
            print(0, end='\t')
        else:
            print(j, end='\t')
    print()

