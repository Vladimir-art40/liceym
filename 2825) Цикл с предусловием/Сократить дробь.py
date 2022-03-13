def gcd_rem_division(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

c = a1 * b2 - a2 * b1
d = b1 * b2
e = gcd_rem_division(c, d)
print(str(int(c / e)) + '/' + str(int(d / e)))

