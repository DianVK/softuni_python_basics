budget = float(input())
count_nightstands = int(input())
price_per_nightstand = float(input())
percent_additional_expense = int(input())

if count_nightstands > 7:
    price_per_nightstand = price_per_nightstand * 0.95

sum_nightstands = count_nightstands * price_per_nightstand
percentage = budget * (percent_additional_expense / 100)
total_sum = sum_nightstands + percentage
diff = abs(budget - total_sum)

if total_sum <= budget:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")
