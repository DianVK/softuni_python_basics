needed_money = float(input())
cash_money = float(input())
count_days = 0
count_days_spend = 0
while cash_money < needed_money:
    if count_days_spend == 5:
        break
    spend_save = input()
    count_days += 1
    sum_spend_save = float(input())
    if spend_save == "spend":
        cash_money -= sum_spend_save
        if cash_money < 0:
            cash_money = 0
        count_days_spend += 1
    elif spend_save == "save":
        cash_money += sum_spend_save
        count_days_spend = 0
if count_days_spend == 5:
    print("You can't save the money.")
    print(f"{count_days}")

if cash_money >= needed_money:
    print(f"You saved the money for {count_days} days.")

