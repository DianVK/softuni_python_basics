# •	Първи ред - напитка - текст с възможности"Espresso", "Cappuccino" или "Tea"
# •	Втори ред - захар - текст  с възможности "Without", "Normal" или "Extra"
# •	Трети ред - брой напитки - цяло число в интервала [1… 50]

kind_of_drink = input()
sugar = input()
count_drinks = int(input())
total_sum = 0
if kind_of_drink == "Espresso":
    if sugar == "Without":
        total_sum += 0.90 * count_drinks
        discount = total_sum * 0.35
        total_sum -= discount
    elif sugar == "Normal":
        total_sum += 1.00
        total_sum = total_sum * count_drinks
    elif sugar == "Extra":
        total_sum += 1.20
        total_sum = total_sum * count_drinks
    if count_drinks >= 5:
        total_sum = total_sum * 0.75
elif kind_of_drink == "Cappuccino":
    if sugar == "Without":
        total_sum += 1.00 * count_drinks
        discount = total_sum * 0.35
        total_sum -= discount
    elif sugar == "Normal":
        total_sum += 1.20
        total_sum = total_sum * count_drinks
    elif sugar == "Extra":
        total_sum += 1.60
        total_sum = total_sum * count_drinks
if kind_of_drink == "Tea":
    if sugar == "Without":
        total_sum += 0.50 * count_drinks
        discount = total_sum * 0.35
        total_sum -= discount
    elif sugar == "Normal":
        total_sum += 0.60
        total_sum = total_sum * count_drinks
    elif sugar == "Extra":
        total_sum += 0.70
        total_sum = total_sum * count_drinks
if total_sum > 15.00:
    total_sum = total_sum * 0.80
print(f"You bought {count_drinks} cups of {kind_of_drink} for {total_sum:.2f} lv.")