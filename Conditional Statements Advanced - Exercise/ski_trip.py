days_to_stay = int(input())
type_room = input()
review = input()
price_per_night = 0
if type_room == "room for one person":
    price_per_night = 18.00
elif type_room == "apartment":
    price_per_night = 25.00
    if days_to_stay < 10:
        price_per_night *= 0.70
    elif 10 == days_to_stay <= 15:
        price_per_night *= 0.65
    else:
        price_per_night *= 0.50
else:
    price_per_night = 35.00
    if days_to_stay < 10:
        price_per_night *= 0.90
    elif 10 == days_to_stay <= 15:
        price_per_night *= 0.85
    else:
        price_per_night *= 0.80
if review == "positive":
    final_price = (days_to_stay - 1) * price_per_night
    final_price *= 1.25
else:
    final_price = (days_to_stay - 1) * price_per_night
    final_price *= 0.90
print(f"{final_price:.2f}")

