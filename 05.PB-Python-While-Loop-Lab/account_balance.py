input_money = (input())
ballance = 0.0
while input_money != "NoMoreMoney":
    amount = float(input_money)
    if amount < 0:
        print("Invalid operation!")
        break
    ballance += amount
    print(f"Increase: {amount:.2f}")
    input_money = input()

print(f"Total: {ballance:.2f} ")

