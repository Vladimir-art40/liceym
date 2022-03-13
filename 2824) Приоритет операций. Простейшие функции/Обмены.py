def compare(s1, s2):
    if s1 < s2:
        return s1, s2
    elif s2 < s1:
        return s2, s1
    return s1, s2


a = int(input())
b = int(input())
c = int(input())

a, b = compare(a, b)
b, c = compare(b, c)
a, b = compare(a, b)
b, c = compare(b, c)

smallest = a
medium = b
largest = c

print(c)
print(b)
print(a)

