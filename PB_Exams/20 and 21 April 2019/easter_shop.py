starting_amount = int(input())
command = input()
count_sold = 0
while command != "Close":
    count_eggs = int(input())
    if command == "Buy":
        if count_eggs > starting_amount:

            print(f"Not enough eggs in store!")
            print(f"You can buy only {starting_amount}.")
            break
        starting_amount -= count_eggs
        count_sold += count_eggs
    elif command == "Fill":
        starting_amount += count_eggs
    command = input()

if command == "Close":
    print(f"Store is closed!")
    print(f"{count_sold} eggs sold.")


