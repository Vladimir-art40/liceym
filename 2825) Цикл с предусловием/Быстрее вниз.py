d = int(input())
out = 0
while (line := int(input())) != 0:
    if line > d:
        out += 1
    d = line
print(out)

