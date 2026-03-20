import math
d, m, y = map(int, input("Nhap ngay, thang va nam: ").split())

# kiểm tra năm nhuận
if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
    nhuan = True
else:
    nhuan = False

# số ngày từng tháng
ngay_thang = [31, 29 if nhuan else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# kiểm tra hợp lệ
if m < 1 or m > 12 or d < 1 or d > ngay_thang[m-1]:
    print("Khong hop le")
else:
    print("Hop le")

    a = (14 - m) // 12
    y1 = y - a
    m1 = m + 12*a - 2

    dayofweek = (d + y1 + y1//4 - y1//100 + y1//400 + (31*m1)//12) % 7

    thu = ["Chu nhat", "Thu 2", "Thu 3", "Thu 4", "Thu 5", "Thu 6", "Thu 7"]

    print(thu[dayofweek])