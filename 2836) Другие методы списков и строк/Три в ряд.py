n = int(input())
lines = ['_'] * n
score = [0, 0]
step = [n // 2, 'R' if n % 2 else 'G']
print('AI step', *step)
turn = 0
lines[step[0]] = step[1]
print(*lines)
while '_' in lines:
    free_indexes = [i for i in range(n) if lines[i] == '_']
    if not turn:
        step = input().split()
        print('Your step', *step)
        if int(step[0]) not in free_indexes:
            print('This place is taken.')
            continue
        elif step[1].upper() not in 'RGB':
            print('Use RGB Letters.')
            continue
    else:
        for i in free_indexes:
            if i < n - 1 and lines[i + 1] != '_':
                step = [i, lines[1 + 1]]
                break
            elif i > 0 and lines[i - 1] != '_':
                step = [i, lines[i - 1]]
                break
        print("AI step", *step)

    turn = (turn + 1) % 2
    lines[int(step[0])] = step[1]
    print(*lines)
    check = [i for i in range(2, n) if lines[i] == lines[i - 1] == lines[i - 2] != '_']
    if check:
        score[turn] += 1
        for index in check:
            lines[index - 2] = '_'
            lines[index - 1] = '_'
            lines[index] = '_'
        print(*lines)

if score[0] > score[1]:
    print('AI win!', score[0], ':', score[1])
elif score[1] > score[0]:
    print('You win!', score[1], ':', score[0])
else:
    print('We have a tie.')

