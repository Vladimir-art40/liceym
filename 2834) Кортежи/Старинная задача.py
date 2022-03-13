b = int(input())
a = int(input())
sum = int(input()) * 120
u = 0
out = ()
for i in range(sum // a, 0, -1):
    if (sum - a * i) % b == 0:
        if i != 0 and (sum - a * i) // b != 0:
            if (i * 5 + (sum - a * i) // b * 2) > u:
                u = (i * 5 + (sum - a * i) // b * 2)
                out = ((sum - a * i) // b, i)
print(u)
print(out)

