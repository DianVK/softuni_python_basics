money_born = float(input())
year_to_live = int(input())
current_year = 17
for i in range(1800, year_to_live + 1):
    if i % 2 == 1:
        current_year += 1
        money_born -= 12000 + (current_year * 50)
    else:
        current_year += 1
        money_born -= 12000
if money_born >= 0:
    print(f"Yes! He will live a carefree life and will have {money_born:.2f} dollars left.")
else:
    print(f"He will need {abs(money_born):.2f} dollars to survive.")