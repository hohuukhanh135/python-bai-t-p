def area(x1, y1, x2, y2, x3, y3):
    return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2
xA, yA = map(float, input("Nhap A(x y): ").split())
xB, yB = map(float, input("Nhap B(x y): ").split())
xC, yC = map(float, input("Nhap C(x y): ").split())
xM, yM = map(float, input("Nhap M(x y): ").split())
S  = area(xA, yA, xB, yB, xC, yC)
S1 = area(xM, yM, xA, yA, xB, yB)
S2 = area(xM, yM, xB, yB, xC, yC)
S3 = area(xM, yM, xC, yC, xA, yA)

if S == ( S1 + S2 + S3 ):
    if S1 == 0 or S2 == 0 or S3 == 0:
        print("M nam tren canh tam giac")
    else:
        print("M nam trong tam giac")
else:
    print("M nam ngoai tam giac")
