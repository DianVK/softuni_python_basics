term_condition = input()
type_contract = input()
internet = input()
count_months = int(input())
price = 0
total_price = 0
if term_condition == "one":
    if type_contract == "Small":
        price = 9.98
    elif type_contract == "Middle":
        price = 18.99
    elif type_contract == "Large":
        price = 25.98
    elif type_contract == "ExtraLarge":
        price = 35.99
    if internet == "yes":
        if price <= 10:
            price += 5.50
        elif price <= 30:
            price += 4.35
        elif price > 30:
            price += 3.85
    total_price = price * count_months
elif term_condition == "two":
    if type_contract == "Small":
        price = 8.58
    elif type_contract == "Middle":
        price = 17.09
    elif type_contract == "Large":
        price = 23.59
    elif type_contract == "ExtraLarge":
        price = 31.79
    if internet == "yes":
        if price <= 10:
            price += 5.50
        elif price <= 30:
            price += 4.35
        elif price > 30:
            price += 3.85
    total_price = (price * count_months)
    total_price = total_price * 0.9625

print(f"{total_price:.2f} lv.")
