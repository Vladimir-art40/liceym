r = []
e = input()
while e != '':
    r.append(e)
    e = input()

t = '@' + input()
print(*sorted([q.lstrip(t).lstrip()[0].upper() + q.lstrip(t).lstrip()[1:] for q in r if q.startswith(t)]), sep='\n')

