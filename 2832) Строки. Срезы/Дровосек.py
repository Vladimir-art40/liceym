sep = input()
k = int(input())
start = False
while len(sep) > k:
    if start:
        print(sep[0:k])
        sep = sep[k:]
    else:
        print(sep[-k:])
        sep = sep[:-k]
    start = not start
print(sep)

