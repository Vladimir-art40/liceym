a = input()
actions = []
for t in set(a):
    start = a.index(t)
    stop = a.rindex(t)
    actions.append((start, 1))
    actions.append((stop, 2))
for i in range(len(a)):
    actions.append((i, 3))
opened_now = 0
worked = 0
actions.sort()
for step in actions:
    if step[1] == 1:
        opened_now += 1
    if step[1] == 2:
        opened_now -= 1
    if step[1] == 3:
        worked += 1
        if opened_now == 0:
            print(worked, end=' ')
            worked = 0

