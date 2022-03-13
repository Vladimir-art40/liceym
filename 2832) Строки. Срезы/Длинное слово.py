a = input()
e = ''
me = ''
for i in a:
    if i == ' ':
        if len(e) > len(me):
            me = e
        e = ''
    else:
        e += i
if len(e) > len(me):
    me = e
print(me)

