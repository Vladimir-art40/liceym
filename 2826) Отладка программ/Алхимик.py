a = int(input())
m = 2.0 * a
d = a / 3.0
e = a / 8.0
n = m + d + e
s = 0
while m + d + e > n / 2:
    m *= 0.99
    e *= 0.995
    s += 1
print(str(s) + ' ' + str(m + d + e))

