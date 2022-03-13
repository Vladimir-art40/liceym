a = int(input())
k = []
for i in range(a):
    name = input()
    data = set()
    now = input()
    while now != 'ВСЕ':
        data.add(now)
        now = input()
    tester = ''
    for r in name:
        tester += chr(ord('а') + ord('Я') - ord(r))
    k.append((len(data), tester, name, data))
first = max(k)
k.remove(first)
second = max(k)
print(first[2])
print(second[2])
print('ОДИНАКОВЫЕ' if first[3] == second[3] else 'РАЗНЫЕ')


