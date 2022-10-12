budget = float(input())
category_ticket = input()
count_people = int(input())
ticket_vip = 499.99
ticket_normal = 249.99
transport = 0
if 1 <= count_people <= 4:
    transport = budget * 0.75
if 5 <= count_people <= 9:
    transport = budget * 0.60
if 10 <= count_people <= 24:
    transport = budget * 0.50
if 25 <= count_people <= 49:
    transport = budget * 0.40
if 50 <= count_people:
    transport = budget * 0.25
left_cash = budget - transport
if category_ticket == "VIP":
    vip_price = ticket_vip * count_people
    if budget < vip_price:
        calculation = budget - vip_price
        print(f"Yes! You have {calculation} leva left.")
    elif budget > vip_price:
        calculation = abs(budget - vip_price)
        print(f"Not enough money! You need {calculation} leva.")
elif category_ticket == "Normal":
    normal_price = ticket_normal * count_people
    if budget < normal_price:
        calculation = budget - normal_price
        print(f"Yes! You have {calculation} leva left.")
    elif budget > normal_price:
        calculation = abs(budget - normal_price)
        print(f"Not enough money! You need {calculation} leva.")


