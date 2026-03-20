def zeller(day, month, year):
    if month < 3:
        month += 12
        year -= 1

    K = year % 100
    J = year // 100

    h = (day + (13 * (month + 1)) // 5 + K + K // 4 + J // 4 + 5 * J) % 7
    return h  # 0 = Thứ 7, 1 = CN, 2 = Thứ 2, ...

def days_in_month(month, year):
    if month == 2:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return 29
        return 28
    if month in [4, 6, 9, 11]:
        return 30
    return 31

year = int(input("Nhập năm (>1582): "))

for month in range(1, 13):
    print(f"\nTháng {month}")
    print("S  M  T  W  T  F  S")

    first = zeller(1, month, year)
    pos = (first + 6) % 7  # Đổi về: 0 = CN

    days = days_in_month(month, year)

    print("   " * pos, end="")

    for d in range(1, days + 1):
        print(f"{d:2}", end=" ")
        if (pos + d) % 7 == 0:
            print()
    print()
