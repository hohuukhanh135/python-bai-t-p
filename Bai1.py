import math

S = float(input("Nhap dien tich S: "))

R = (S/(4*math.pi))**0.5
V = 4/3*math.pi*R**3

print("The tich V =", round(V,6))
