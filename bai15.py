import math
d, m, y = map(int, input("Nhap ngay, thang, nam: ").split())

# kiểm tra năm nhuận
if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
    nhuan = True
else:
    nhuan = False

# công thức tính ngày thứ bao nhiêu
s = int(30.42 * (m - 1)) + d

if m == 2 or (nhuan and m > 2):
    s = s + 1

if 2 < m < 8:
    s = s - 1

print("Ngay thu:", s)