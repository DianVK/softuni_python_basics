budget = float(input())
count_statists = int(input())
price_clothes_for_one = float(input())
decor_price = budget * 0.10
if count_statists > 150:
    price_clothes_for_one = price_clothes_for_one - (price_clothes_for_one * 0.10)
sum_decor_and_clothes = (price_clothes_for_one * count_statists) + decor_price
money_left = abs(budget - sum_decor_and_clothes)
if budget >= sum_decor_and_clothes:
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
else:
    print(f"Not enough money!")
    print(f"Wingard needs {money_left:.2f} leva more.")