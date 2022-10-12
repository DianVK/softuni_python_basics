type_fuel = input()
amount_liters = float(input())
club_card = input()
gasoline = 2.22
diesel = 2.33
gas = 0.93
total_price = 0
if type_fuel == "Gas" and club_card == "Yes":
    total_price = (gas - 0.08) * amount_liters
elif type_fuel == "Gasoline" and club_card == "Yes":
    total_price = (gasoline - 0.18) * amount_liters
elif type_fuel == "Diesel" and club_card == "Yes":
    total_price = (diesel - 0.12) * amount_liters
else:
    if type_fuel == "Gas":
        total_price = gas * amount_liters
    elif type_fuel == "Gasoline":
        total_price = gasoline * amount_liters
    elif type_fuel == "Diesel":
        total_price = diesel * amount_liters
if 20 <= amount_liters <= 25:
    total_price *= 0.92
elif amount_liters > 25:
    total_price *= 0.90
print(f"{total_price:.2f} lv.")