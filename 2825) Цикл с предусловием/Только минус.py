d = 0
while (line := input()) != "":
    if '-' in line:
        d += 1
        continue
    if float(line) > 36.6:
        break
print(d)


