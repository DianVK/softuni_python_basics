count_guests = int(input())
price_per_person = float(input())
budget = float(input())

if 10 <= count_guests <= 15:
    price_per_person = price_per_person * 0.85
elif 15 < count_guests <= 20:
    price_per_person = price_per_person * 0.80
elif count_guests > 20:
    price_per_person = price_per_person * 0.75

price_cake = budget * 0.10

total_price = (price_per_person * count_guests) + price_cake
diff = abs(budget - total_price)
if budget > total_price:
    print(f"It is party time! {diff:.2f} leva left.")
else:
    print(f"No party! {diff:.2f} leva needed.")


