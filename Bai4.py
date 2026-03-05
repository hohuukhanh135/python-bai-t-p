import math
#bai4
a, b, c = map(float, input("Nhap 3 canh a b c: ").split())

if a + b <= c or a + c <= b or b + c <= a:
    print("Khong phai tam giac hop le")
else:
    print("Tam giac hop le")
    if a == b == c:
        loai = "tam giac deu"
    elif a == b or a == c or b == c:
        loai = "tam giac can"
    elif a*a + b*b == c*c or \
         a*a + c*c == b*b or \
         b*b + c*c == a*a:
        loai = "tam giac vuong"
    else:
        loai = "tam giac thuong"

    print("Loai tam giac :", loai)
    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))

    print("Dien tich S = ", S)
