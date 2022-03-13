n = int(input())
c_list = dict()
for _ in range(n):
    o = input().split()
    c_list[o[0]] = (int(o[1]), int(o[2]))
t = sum(map(int, input().split()))
for col, gran in c_list.items():
    if gran[0] <= t <= gran[1]:
        print(col)

