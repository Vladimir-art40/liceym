n = int(input())
jumps = [int(input()) for i in range(n)]
lines = [input() for i in range(n)]
ok = True
out = ''
for t in range(len(lines)):
    was = False
    for ch in lines[t]:
        num = 0
        for y in lines[t]:
            if y == ch:
                num += 1
        if num == jumps[t]:
            if not was:
                was = True
                out += ch
            else:
                if ch != out[-1]:
                    ok = False
                    break
    if not was:
        ok = False
        break
if ok:
    print(out)
else:
    print('нечленораздельно')

