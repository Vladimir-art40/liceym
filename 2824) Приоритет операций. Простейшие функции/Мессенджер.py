import math


n = int(input())
m = int(input())
a = input()
cost = math.ceil(len(a) / m) * n
print(cost)

