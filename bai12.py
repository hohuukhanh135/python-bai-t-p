import math
a1, b1, c1 = map(float, input("Nhap a1, b1, c1: ").split())
a2, b2, c2 = map(float, input("Nhap a2, b2, c2: ").split())

D = a1*b2 - a2*b1
Dx = c1*b2 - c2*b1
Dy = a1*c2 - a2*c1

if D != 0:
    x = Dx / D
    y = Dy / D
    print("x =", x)
    print("y =", y)
else:
    if Dx == 0 and Dy == 0:
        print("He phuong trinh vo so nghiem")
    else:
        print("He phuong trinh vo nghiem")