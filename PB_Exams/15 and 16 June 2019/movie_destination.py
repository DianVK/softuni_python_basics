budget = float(input())
destination = input()
season = input()
count_days = int(input())
price = 0
if destination == "Dubai":
    if season == "Winter":
        price = 45000
    elif season == "Summer":
        price = 40000
elif destination == "Sofia":
    if season == "Winter":
        price = 17000
    elif season == "Summer":
        price = 12500
elif destination == "London":
    if season == "Winter":
        price = 24000
    elif season == "Summer":
        price = 20250

total_price = count_days * price
if destination == "Dubai":
    total_price = total_price * 0.70
elif destination == "Sofia":
    total_price = total_price * 1.25

calculation = abs(budget - total_price)
if budget > total_price:
    print(f"The budget for the movie is enough! We have {calculation:.2f} leva left!")
else:
    print(f"The director needs {calculation:.2f} leva more!")
