d = int(input())
while d % 10 == 0:
    d //= 10
o = ''
for f in str(d):
    o = f + o
print(o)

