def compare(s1, s2):
    if len(s1) < len(s2):
        return s1, s2
    elif len(s2) < len(s1):
        return s2, s1
    for d in range(len(s1)):
        if s1[d] < s2[d]:
            return s1, s2
        elif s2[d] < s1[d]:
            return s2, s1
    return s1


a = input()
b = input()
c = input()

a, b = compare(a, b)
b, c = compare(b, c)
a, b = compare(a, b)
b, c = compare(b, c)

print(a)
print(b)
print(c)

