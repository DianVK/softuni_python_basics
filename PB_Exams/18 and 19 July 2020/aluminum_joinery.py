
count_windows = int(input())
size_windows = input()
delivery = input()
price = 0

if count_windows <= 10:
    print("Invalid order")
    exit()

if size_windows == "90X130":
    price = 110
    price = price * count_windows
    if count_windows > 60:
        price = price * 0.92
    elif count_windows > 30:
        price = price * 0.95
elif size_windows == "100X150":
    price = 140
    price = price * count_windows
    if count_windows > 80:
        price = price * 0.90
    elif count_windows > 40:
        price = price * 0.94
elif size_windows == "130X180":
    price = 190
    price = price * count_windows
    if count_windows > 50:
        price = price * 0.88
    elif count_windows > 20:
        price = price * 0.93
elif size_windows == "200X300":
    price = 250
    price = price * count_windows
    if count_windows > 50:
        price = price * 0.86
    elif count_windows > 25:
        price = price * 0.91


if delivery == "With delivery":
    price += 60
elif delivery == "Without delivery":
    price = price
if count_windows >= 100:
    price = price * 0.96
print(f"{price:.2f} BGN")

