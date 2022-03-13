a = int(input())
counter = a + 1
for i in range(4):
    a = a + counter
    a = a * (counter + 1)
    counter += 2
print(a)

