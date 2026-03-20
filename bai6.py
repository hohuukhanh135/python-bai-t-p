import math
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

t = 0   # biến phụ

if a > b:
    t = a
    a = b
    b = t

if a > c:
    t = a
    a = c
    c = t

if b > c:
    t = b
    b = c
    c = t

print("Tăng dần:", a, b, c)