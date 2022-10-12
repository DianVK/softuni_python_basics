deposit = float(input())
months = int(input())
year_increase_percent = float(input())
calculation = deposit * year_increase_percent/100
secondcalculations = calculation / 12
amount = deposit + (months * secondcalculations)
print(amount)
