a = input()
num = int(input())
maxLen = 0
lenNow = 0
good = False
for k in range(num):
    r = input()
    if r == a:
        lenNow += 1
    else:
        maxLen = max(maxLen, lenNow)
        lenNow = 0
print(max(maxLen, lenNow))

