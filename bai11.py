import random

human = 0
computer = 0

while True:
    x = input("Nhap ky tu (b-d-k), ky tu khac de thoat: ")

    if x not in ["b", "d", "k"]:
        break

    may = random.choice(["b", "d", "k"])
    print("Computer:", may)

    if x == may:
        print("Hoa")
    elif (x == "b" and may == "d") or (x == "d" and may == "k") or (x == "k" and may == "b"):
        human += 1
    else:
        computer += 1

    print("Ty so human - computer:", human, "-", computer)