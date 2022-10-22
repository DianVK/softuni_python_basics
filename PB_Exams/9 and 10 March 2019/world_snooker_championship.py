stage_finals = input()
type_ticket = input()
count_tickets = int(input())
photo = input()
price_ticket = 0
for ticket in range(1):
    if stage_finals == "Quarter final":
        if type_ticket == "Standard":
            price_ticket = 55.50
        elif type_ticket == "Premium":
            price_ticket = 105.20
        elif type_ticket == "VIP":
            price_ticket = 118.90

    elif stage_finals == "Semi final":
        if type_ticket == "Standard":
            price_ticket = 75.88
        elif type_ticket == "Premium":
            price_ticket = 125.22
        elif type_ticket == "VIP":
            price_ticket = 300.40

    elif stage_finals == "Final":
        if type_ticket == "Standard":
            price_ticket = 110.10
        elif type_ticket == "Premium":
            price_ticket = 160.66
        elif type_ticket == "VIP":
            price_ticket = 400

price = count_tickets * price_ticket

if photo == "Y" and price > 4000:
    price = price


if price > 4000:
    price = price * 0.75
elif price > 2500:
    price = price * 0.90

if photo == "Y" and price < 4000:
    price += 40 * count_tickets

print(f"{price:.2f}")
