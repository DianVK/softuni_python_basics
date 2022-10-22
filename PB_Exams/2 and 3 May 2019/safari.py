# •	Цената на един литър гориво е 2.10 лв.
# •	Цената за екскурзовод е 100лв.
# •	В зависимост от деня има отстъпки от общата цена - за събота 10%, а за неделя 20%

budget = float(input())
liters_fuel_needed = float(input())
day_from_week = input()

price_per_liter = 2.10
price_for_leader = 100

total_price = (liters_fuel_needed * price_per_liter) + price_for_leader

if day_from_week == "Saturday":
    total_price = total_price * 0.90
elif day_from_week == "Sunday":
    total_price = total_price * 0.80

diff = abs(budget - total_price)
if budget >= total_price:
    print(f"Safari time! Money left: {diff:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")

