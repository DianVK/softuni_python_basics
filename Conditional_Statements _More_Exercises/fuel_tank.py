fuel = input().lower()
liters_fuel = float(input())
if fuel == "diesel" or fuel == "gasoline" or fuel == "gas":
    if liters_fuel >= 25:
        print(f"You have enough {fuel}.")
    elif liters_fuel < 25:
        print(f"Fill your tank with {fuel}!")
else:
    print("Invalid fuel!")