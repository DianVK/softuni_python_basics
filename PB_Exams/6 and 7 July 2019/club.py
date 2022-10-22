wanted_profit = float(input())
name_of_cocktail = input()
total_price = 0.00
money = 0.00
while name_of_cocktail != "Party!":
    count_of_cocktails = int(input())
    price_of_cocktail = len(name_of_cocktail)
    total_price = price_of_cocktail * count_of_cocktails
    if total_price % 2 != 0:
        total_price = total_price - (total_price * 0.25)

    money += total_price

    if money >= wanted_profit:
        print("Target acquired.")
        break

    name_of_cocktail = input()

    if name_of_cocktail == "Party!":
        diff = wanted_profit - money
        print(f"We need {diff:.2f} leva more.")

print(f"Club income - {money:.2f} leva.")