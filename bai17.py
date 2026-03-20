def zeller(day, month, year):
    if month < 3:
        month += 12
        year -= 1
    K = year % 100
    J = year // 100
    return (day + (13*(month+1))//5 + K + K//4 + J//4 + 5*J) % 7

def days_in_month(month, year):
    if month == 2:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return 29
        return 28
    if month in [4, 6, 9, 11]:
        return 30
    return 31

year = int(input())
start_day = int(input())
month = int(input())

people = ["A", "B", "C", "D", "E"]

first = zeller(1, month, year)
pos = (first + 6) % 7

total_days = 0
for m in range(1, month):
    total_days += days_in_month(m, year)

print("Sun Mon Tue Wed Thu Fri Sat")

print("    " * pos, end="")

days = days_in_month(month, year)

for d in range(1, days + 1):
    index = (total_days + d - 1) % 5
    person = people[index]
    print(f"{d:2}[{person}]", end=" ")
    if (pos + d) % 7 == 0:
        print()

print()