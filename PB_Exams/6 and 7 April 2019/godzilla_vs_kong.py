budget = float(input())
count_statists = int(input())
price_of_clothes_per_statist = float(input())
decor = budget * 0.10
if count_statists > 150:
    price_of_clothes_per_statist = price_of_clothes_per_statist * 0.90
expenses = (price_of_clothes_per_statist * count_statists) + decor

if expenses > budget:
    print(f"Not enough money!")
    print(f"Wingard needs {(expenses - budget):.2f} leva more.")
elif expenses <= budget:
    print(f"Action!")
    print(f"Wingard starts filming with {(budget - expenses):.2f} leva left.")
