a = input()
s1 = 0
s2 = 0
i = 0
for g in a:
    if i > 0:
        i -= 1
        continue
    if g == 'к':
        s1 += 1
    if g == 'с':
        s2 += 1
s = s1 * 3 - (s2 - 1) * 2
if s >= 0:
    print(int(str(10 ** s)))
else:
    print('1/' + str(10 ** (-s)))

