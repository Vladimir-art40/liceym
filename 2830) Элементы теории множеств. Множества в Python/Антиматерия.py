all = set()
was = []
i = input()
now_read = set()
while i != '':
    o = int(i)
    if o == -1:
        was.append(now_read)
        now_read = set()
    else:
        all.add(o)
        now_read.add(o)
    i = input()

for t in all:
    ins = 0
    for u in was:
        if t in u:
            ins += 1
    if ins == 1:
        print(t, end=' ')
        

