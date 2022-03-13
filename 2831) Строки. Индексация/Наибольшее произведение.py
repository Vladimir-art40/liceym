t = input()
e = 0
for i in range(len(t) - 4):
    if int(t[i]) * int(t[i + 1]) * int(t[i + 2]) * int(t[i + 3]) * int(t[i + 4]) > e:
        e = int(t[i]) * int(t[i + 1]) * int(t[i + 2]) * int(t[i + 3]) * int(t[i + 4])
print(e)

