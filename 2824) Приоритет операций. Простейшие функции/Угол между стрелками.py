a = int(input())
b = int(input())
c = 360 / 12 * (a % 12) + 360 / 12 / 60 * (b % 60)
f = 360 / 60 * (b % 60)
print(abs(c - f) % 360)

