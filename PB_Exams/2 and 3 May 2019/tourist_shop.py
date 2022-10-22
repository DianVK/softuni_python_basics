budget = float(input())
countProducts = 0
totalSum = 0
command = input()
while command != "Stop":
    price = float(input())
    countProducts += 1
    if countProducts % 3 == 0:
        price = price / 2

    totalSum += price

    if totalSum > budget:
        print("You don't have enough money!")
        needMoney = totalSum - budget
        print(f"You need {needMoney:.2f} leva!")
        break
    command = input()

if command == "Stop":
    print(f"You bought {countProducts} products for {totalSum:.2f} leva.")
