import math

x = float(input("Nhập số đo x của góc (phút): "))
degree = x / 60
goc_vuong = int(degree // 90) + 1
if goc_vuong > 4:
    goc_vuong = goc_vuong % 4
    if goc_vuong == 0:
        goc_vuong = 4

print("x thuộc góc vuông thứ", goc_vuong)
rad = degree * math.pi / 180
cosx = math.cos(rad)
print("cos(x) =", cosx)