h = int(input())
m = int(input())
n = int(input())
g = (12 - h) * 60 - m
k = g // n
if k < 1:
    print('Не останавливаемся!')
else:
    print(str(k) + ' минут')

