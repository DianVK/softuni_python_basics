budget = float(input())
count_serials = int(input())
for serial in range(1, count_serials + 1):
    name_of_serial = input()
    price_for_serial = float(input())
    if name_of_serial == "Thrones":
        price_for_serial = price_for_serial * 0.50
        budget -= price_for_serial
    elif name_of_serial == "Lucifer":
        price_for_serial = price_for_serial * 0.60
        budget -= price_for_serial
    elif name_of_serial == "Protector":
        price_for_serial = price_for_serial * 0.70
        budget -= price_for_serial
    elif name_of_serial == "TotalDrama":
        price_for_serial = price_for_serial * 0.80
        budget -= price_for_serial
    elif name_of_serial == "Area":
        price_for_serial = price_for_serial * 0.90
        budget -= price_for_serial
    else:
        budget -= price_for_serial


if budget >= 0:
    print(f"You bought all the series and left with {budget:.2f} lv.")
else:
    print(f"You need {abs(budget):.2f} lv. more to buy the series!")


