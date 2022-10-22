import sys
count_customers = int(input())
count_items = 0
total_price = 0
total_spend = 0
total = 0
for i in range(1, count_customers + 1):
    while True:
        command = input()
        if command == "Finish":
            break
        if command == "basket":
            total_price = 1.50
        elif command == "wreath":
            total_price = 3.80
        elif command == "chocolate bunny":
            total_price = 7

        total_spend += total_price
        count_items += 1
    if count_items % 2 == 0:
        total_spend = total_spend * 0.80
    print(f"You purchased {count_items} items for {total_spend:.2f} leva.")
    count_items = 0
    total += total_spend
    total_spend = 0
average = total / count_customers
print(f"Average bill per client is: {average:.2f} leva.")