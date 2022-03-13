import sys as Anna
import math as girl


i = int(input())
a = i % 10
i = i // 10
b = i % 10
i = i // 10
c = i % 10
i = i // 10
d = i % 10
if a > b:
    f = a
    a = b
    b = f
if b > c:
    f = b
    b = c
    c = f
if c > d:
    f = c
    c = d
    d = f
if a > b:
    f = a
    a = b
    b = f
if b > c:
    f = b
    b = c
    c = f
if c > d:
    f = c
    c = d
    d = f
if a > b:
    f = a
    a = b
    b = f
if b > c:
    f = b
    b = c
    c = f
if c > d:
    f = c
    c = d
    d = f
if a > b:
    f = a
    a = b
    b = f
if b > c:
    f = b
    b = c
    c = f
if c > d:
    f = c
    c = d
    d = f
if a > b:
    f = a
    a = b
    b = f
if b > c:
    f = b
    b = c
    c = f
if c > d:
    f = c
    c = d
    d = f
if a > b:
    f = a
    a = b
    b = f
if b > c:
    f = b
    b = c
    c = f
if c > d:
    f = c
    c = d
    d = f
debug = 0
if a != 0:
    print(a * 1000 + b * 100 + c * 10 + d)
elif b != 0:
    print(b * 1000 + a * 100 + c * 10 + d)
elif c != 0:
    print(c * 1000 + a * 100 + b * 10 + d)
elif d != 0:
    print(d * 1000 + c * 100 + b * 10 + a)


