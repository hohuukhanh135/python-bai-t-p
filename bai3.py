import math

xC, yC = map(float, input("Nhap C(xC yC): ").split())
R = float(input("Nhap ban kinh R: "))
xM, yM = map(float, input("Nhap M(xM yM): ").split())

CM = math.sqrt((xM - xC)**2 + (yM - yC)**2)

if CM == R :
    print("M nam tren duong tron")
elif CM < R:
    print("M nam trong duong tron")
else:
    print("M nam ngoai duong tron")
