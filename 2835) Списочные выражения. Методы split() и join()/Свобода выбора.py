a = input().split()
f = a[0]
num = int(a[1])
data = a[2].split(f)
g = [e for e in data if len(set(e)) >= num]
print(*g, sep=f[::-1])

