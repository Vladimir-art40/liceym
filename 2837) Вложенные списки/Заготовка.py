p = [[0] * 10 for _ in range(10)]
li = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
nm = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'к']
for i in range(10):
    raw_data = input().split()
    horiz = raw_data[1] == 'г'
    poz_x = nm.index(raw_data[0][0])
    poz_y = int(raw_data[0][1:]) - 1
    for j in range(li[i]):
        if horiz:
            p[poz_y][poz_x + j] = '□'
        else:
            p[poz_y + j][poz_x] = '□'

for line in p:
    print(*line)

