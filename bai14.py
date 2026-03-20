import math
d, m, y = map(int, input("Nhap ngay, thang, nam: ").split())

# kiểm tra năm nhuận
if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
    ngay_thang = [31,29,31,30,31,30,31,31,30,31,30,31]
else:
    ngay_thang = [31,28,31,30,31,30,31,31,30,31,30,31]

# ---- ngày tiếp theo ----
d1, m1, y1 = d, m, y
d1 += 1

if d1 > ngay_thang[m-1]:
    d1 = 1
    m1 += 1
    if m1 > 12:
        m1 = 1
        y1 += 1

print("Ngay mai:", d1, "/", m1, "/", y1)

# ---- ngày hôm qua ----
d2, m2, y2 = d, m, y
d2 -= 1

if d2 == 0:
    m2 -= 1
    if m2 == 0:
        m2 = 12
        y2 -= 1
    d2 = ngay_thang[m2-1]

print("Hom qua:", d2, "/", m2, "/", y2)