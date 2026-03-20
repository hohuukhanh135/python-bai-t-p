import math

while True:
    sin = input("SIN (0 de thoat): ")

    if sin == "0":
        break

    s1 = 0
    s2 = 0

    # tính s1 (vị trí lẻ)
    for i in range(0, 8, 2):
        s1 += int(sin[i])

    # tính s2 (vị trí chẵn nhân đôi)
    for i in range(1, 8, 2):
        t = int(sin[i]) * 2
        if t >= 10:
            t = t//10 + t%10
        s2 += t

    check = int(sin[8])

    if (s1 + s2 + check) % 10 == 0:
        print("SIN hop le!")
    else:
        print("SIN khong hop le!")