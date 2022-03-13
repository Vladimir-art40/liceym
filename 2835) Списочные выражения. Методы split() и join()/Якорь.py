a = input().split('/')
k = [f.split('#')[0] for f in a if '#' in f]
print(*k)

