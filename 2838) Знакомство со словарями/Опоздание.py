import datetime

buses = dict()
a = input()
while a != '':
    t = a.split()
    if t[0] in buses:
        buses[t[0]].append(datetime.datetime.strptime(t[1], '%H:%M'))
    else:
        buses[t[0]] = [datetime.datetime.strptime(t[1], '%H:%M')]
    a = input()

time_now = datetime.datetime.strptime(input(), '%H:%M')
good = input().split()
min_time = 1000000
for bus in good:
    for time in buses[bus]:
        if time > time_now:
            delta = (time - time_now).total_seconds() // 60 - 6
            if delta < 0:
                continue
            min_time = min(delta, min_time)
if min_time < 1000000:
    print(int(min_time))
else:
    print('None')

